<img width="2048" height="1024" alt="Gemini_Generated_Image_rpxf3krpxf3krpxf" src="https://github.com/user-attachments/assets/12a1d997-bb02-4826-9026-a262968793d6" />


# SleepSensor
An application which monitors the person's eyes and alarm if both eyes are closed for more than 10 seconds ( Considers the person is asleep). 


## Overview
This project is a real-time Drowsiness Detection System built using Python and OpenCV. It is designed to help prevent accidents by monitoring a user's eyes and detecting signs of drowsiness. When the system detects that the user's eyes have been closed for a prolonged period, it triggers an audible alarm to alert them.

It can also be used in different domains like: 
- Education : to check if the pupil fell asleep in his study time.
- Medical : to sense if an uncosious patient has regained consiousness etc.

This application is a great example of a practical computer vision project that leverages Haar Cascades for object detection.

## Features
- Real-time Detection: The system processes video frames in real-time from your webcam to monitor your face and eyes.

- Drowsiness Alarm: An audible alarm is triggered when the system detects that the user's eyes have been closed for a predefined number of consecutive frames.

- Adjustable Sensitivity: The detection sensitivity can be easily configured by changing a single variable in the code.

- Customizable Audio: The alarm sound can be customized by simply replacing the alarmaudio.mp3 file.

## Technologies Used :
- Python

- OpenCV (cv2)

- Pygame

# Setup and Installation
- Step 1: Clone the Repository
First, clone this repository to your local machine:
https://github.com/hrithikvinayakr/SleepSensor
cd eye-monitor

- Step 2: Set up the Virtual Environment
It's recommended to work within a virtual environment.
python -m venv venv
# On Windows
.\venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

- Step 3: Install Dependencies
Install the required Python libraries using pip:
pip install opencv-python pygame

- Step 4: Download Haar Cascade Files
The program requires two XML files for face and eye detection. Download the following files and place them directly into the eye-monitor project folder:
haarcascade_frontalface_default.xml
haarcascade_eye.xml

- Step 5: Add a Custom Alarm Audio
Place your desired alarm audio file in the project folder and name it alarmaudio.mp3.

## How to Run
With all dependencies installed and files in place, run the main.py script from your terminal:
python main.py
The application will start, and a window with your camera feed will appear. To exit the application, press the q key.

## Demonstration
Here are a few screenshots and a video demonstrating the system in action.



- Technical part in VSCode:

<img width="1365" height="767" alt="Screenshot 2025-08-12 235846" src="https://github.com/user-attachments/assets/5a7403af-d7ca-4986-bf64-d14a3457d53c" />



- Project detecting open eyes:

<img width="1365" height="767" alt="Screenshot 2025-08-12 235733" src="https://github.com/user-attachments/assets/426ef6f8-a592-4df0-97ee-c0930f5281f6" />



- Project detecting eyes closed with time period by counting frames:

<img width="1365" height="767" alt="Screenshot 2025-08-12 235806" src="https://github.com/user-attachments/assets/e61454d1-37c5-404d-804b-864d07144ea4" />

Click the link below to watch the video demonstration:
https://drive.google.com/drive/folders/1pwGZE5e3wBB7Ves03e6DXMpCaBpwLGj9?usp=drive_link

## Customization
You can adjust the sensitivity of the drowsiness detection by changing the CONSECUTIVE_FRAMES_THRESHOLD variable in the main.py file. A higher value will require the eyes to be closed for a longer period before the alarm is triggered.


License
This project is licensed under the MIT License.
