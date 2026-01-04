# 🚗 Driver Drowsiness Detection System using OpenCV & MediaPipe

This project is a real-time Driver Drowsiness Detection System designed to monitor a driver’s alertness using computer vision techniques. It analyzes facial landmarks captured through a webcam to detect signs of drowsiness such as eye closure and yawning. When drowsiness is detected, the system generates a voice alert to warn the driver and reduce the risk of accidents.
The system uses MediaPipe Face Mesh to extract facial landmarks from live video frames. Eye openness is calculated using distances between eye landmarks, while yawning is detected by measuring mouth opening ratios. Based on predefined threshold values, the driver’s state is classified as Alert, Drowsy (Eyes Closed), or Yawning (Sleepy). A text-to-speech engine is integrated with a cooldown mechanism to avoid continuous alerts.
Technologies used in this project include Python, OpenCV for real-time video processing, MediaPipe for facial landmark detection, and pyttsx3 for text-to-speech voice alerts. The system is lightweight, efficient, and does not require any deep learning models.

Project Structure:
Driver-Drowsiness-Detection/
│
├── drowsiness_detection.py
├── README.md
└── requirements.txt

Requirements:
- Python 3.x
- opencv-python
- mediapipe
- pyttsx3

To run the project, clone the repository, navigate to the project directory, and execute the Python file. The live webcam feed will display the driver’s current status on the screen. Press the 'Q' key to exit the application.

Applications:
- Driver safety and accident prevention systems  
- Real-time monitoring for long-distance and night-time drivers  
- Fleet management and transport safety solutions  
- Fatigue detection for machine operators and control room staff  
- Educational and research projects in computer vision and human behavior analysis  

Future Enhancements:
- Implementation of Eye Aspect Ratio (EAR) for more accurate eye-closure detection  
- Head pose estimation to detect inattentiveness  
- Logging and storing drowsiness events for analysis  
- Integration with mobile applications or IoT-based alert systems  
- Improved accuracy using machine learning or deep learning models  
- Multi-face detection and support for multiple drivers  

