# Real-Time Face Detection with Python and OpenCV

## Overview
This project is a simple real-time face detection application using Python and OpenCV. It captures video from your webcam, detects human faces in the video stream, and draws green rectangles around each detected face. The application is interactive and runs in a window until you decide to quit.

## Features
- Detects any human face appearing in the webcam video feed.
- Draws bounding rectangles around detected faces.
- Real-time detection with live webcam feed.
- Easy to use and customize.

## Requirements
- Python 3.x
- OpenCV Python library

## Installation
Install the required Python package using pip:
pip install opencv-python

## Usage
1. Save the provided Python script (e.g., `face_recognition_tool.py`).
2. Run the script: python face_recognition_tool.py


3. Your webcam window will open, and faces detected will be highlighted with green rectangles.
4. Press the 'q' key to quit and close the application.

## Code Explanation
- Uses OpenCV's pre-trained Haar Cascade classifier for face detection.
- Converts video frames to grayscale because Haar Cascades work on grayscale images.
- Detects faces using `detectMultiScale` function.
- Draws rectangles around faces with `cv2.rectangle`.
- Shows live video with annotations until user exits.

## Potential Enhancements
- Add face recognition capabilities.
- Log detection timestamps.
- Trigger alerts for unknown faces.
- Integrate with security systems for access control.

## License
This project is open-source and free to use for educational and personal purposes.

---

Enjoy using face detection with Python and OpenCV! Feel free to extend and customize as per your needs.
