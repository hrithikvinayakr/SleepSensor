import cv2
import pygame
import time

# Initialize pygame mixer for playing sound
pygame.mixer.init()

# Load the alarm sound file. This has been updated to use "alarmaudio.mp3"
# as per your request. Make sure this file is in the same directory.
try:
    sound = pygame.mixer.Sound("alarmaudio.mp3")
except pygame.error as e:
    print(f"Error loading sound file: {e}")
    # Create a dummy sound object to prevent the program from crashing
    class DummySound:
        def play(self):
            print("Alarm sound not found. Playing a dummy sound.")
        def stop(self):
            pass
    sound = DummySound()

# Path to the Haar Cascade XML file for face detection.
# Make sure you have downloaded 'haarcascade_frontalface_default.xml'
face_cascade_path = 'haarcascade_frontalface_default.xml'
# Path to the Haar Cascade XML file for eye detection.
# This one is usually located in the same directory as the face cascade.
eye_cascade_path = 'haarcascade_eye.xml'

# Load the Haar Cascade classifiers
try:
    face_cascade = cv2.CascadeClassifier(face_cascade_path)
    eye_cascade = cv2.CascadeClassifier(eye_cascade_path)
    if face_cascade.empty() or eye_cascade.empty():
        raise IOError("Could not load one of the Haar Cascade files.")
except IOError as e:
    print(f"Error loading cascade files: {e}")
    print("Please ensure 'haarcascade_frontalface_default.xml' and 'haarcascade_eye.xml' are in the project folder.")
    exit()

# Start video capture from the default camera
# The argument `0` refers to the primary webcam
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

# --- MODIFIED LOGIC FOR MORE STABLE DETECTION ---
# New variable to count consecutive frames without eye detection.
consecutive_eyes_closed_frames = 0
# A threshold for how many consecutive frames without eyes trigger the alarm.
# A value of 45 is a more robust starting point (approx. 1.5 seconds at 30 fps).
# You can adjust this value to your preference.
CONSECUTIVE_FRAMES_THRESHOLD = 45
is_alarm_playing = False
# --- END MODIFIED LOGIC ---

# Set a font for displaying text on the screen
font = cv2.FONT_HERSHEY_SIMPLEX

# Main loop to continuously capture and process frames from the camera
while True:
    # Read a frame from the video capture
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to grayscale for faster processing
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    # `scaleFactor` decreases the size of the image at each image scale
    # `minNeighbors` specifies how many neighbors each candidate rectangle should have
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Loop through all detected faces
    for (x, y, w, h) in faces:
        # Draw a rectangle around the detected face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
        # Define the region of interest (ROI) for the face
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # Detect eyes within the face ROI
        # Increased minNeighbors from 5 to 10 for a stricter detection, reducing false positives.
        eyes = eye_cascade.detectMultiScale(roi_gray, minNeighbors=10)
        
        # Check if eyes were detected
        if len(eyes) == 0:
            # If no eyes are detected, increment the counter
            consecutive_eyes_closed_frames += 1

            # Check if the counter exceeds the threshold and the alarm isn't playing
            if consecutive_eyes_closed_frames > CONSECUTIVE_FRAMES_THRESHOLD and not is_alarm_playing:
                sound.play()
                is_alarm_playing = True
            
            # Display a warning message
            cv2.putText(frame, "EYES CLOSED!", (20, 50), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
            cv2.putText(frame, f"Frames: {consecutive_eyes_closed_frames}", (20, 80), font, 0.7, (0, 0, 255), 2, cv2.LINE_AA)
        else:
            # If eyes are detected, reset the counter
            consecutive_eyes_closed_frames = 0
            if is_alarm_playing:
                sound.stop()
                is_alarm_playing = False

            # Draw rectangles around the detected eyes
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
            
            # Display a status message
            cv2.putText(frame, "Eyes Open", (20, 50), font, 1, (0, 255, 0), 2, cv2.LINE_AA)

    # Display the processed frame
    cv2.imshow('Drowsiness Detector', frame)

    # Press 'q' to exit the application
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and destroy all windows
cap.release()
cv2.destroyAllWindows()
