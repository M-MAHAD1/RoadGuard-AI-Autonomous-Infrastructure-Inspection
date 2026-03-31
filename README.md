# 🛣️ RoadGuard AI: Autonomous Infrastructure Inspection

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![YOLOv8](https://img.shields.io/badge/YOLO-v8-yellow?logo=yolo&logoColor=black)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?logo=opencv&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

## 📋 Table of Contents
- [About the Project](#-about-the-project)
- [Key Features](#-key-features)
- [System Architecture](#-system-architecture)
- [Project Structure](#-project-structure)
- [Getting Started (Installation & Setup)](#-getting-started)
- [How to Use](#-how-to-use)
- [Model Training Details](#-model-training-details)

---

## 🚀 About the Project
Maintaining roads, highways, and bridges is a costly, time-consuming, and dangerous process when done manually. **RoadGuard AI** is an automated Computer Vision inspection system designed to speed up this process. 

By ingesting video feeds from drones or vehicle dashcams, this system uses a custom-trained Deep Learning model to automatically detect, highlight, and count structural defects like **potholes** in real-time. This tool enables proactive maintenance and generates annotated video reports automatically.

---

## ✨ Key Features
1. **Real-Time Defect Detection:** Processes video frames on-the-fly to identify road hazards.
2. **Smart Status Alerts:** Dynamically updates the screen with text alerts (`GOOD ROAD` vs `BAD ROAD`) based on the presence of defects.
3. **Live Defect Counting:** Displays the exact number of potholes/defects found in the current frame.
4. **Automated Reporting:** Automatically exports an annotated `.mp4` video file showing all detected issues for engineering review.
5. **Lightweight & Fast:** Built using YOLOv8n (Nano), making it highly optimized for fast inference on local machines.

---

## 🧠 System Architecture
1. **Data Ingestion:** Video footage (`input.mp4`) is loaded using OpenCV.
2. **Inference Engine:** Each frame is passed through the custom YOLOv8 model (`best.pt`).
3. **Logic & Annotation:** Bounding boxes are drawn around detected defects. A logic gate checks the defect count to assign a "Status" to the frame.
4. **Output Generation:** The processed frame is displayed live and simultaneously written to an output video file (`output_result.mp4`).

---

## 💻 Getting Started
Follow these steps to set up and run the project on your local machine (Windows/Mac/Linux).

### Prerequisites
Make sure you have **Python 3.8+** installed on your system.

### Installation Steps
1. Clone this repository or download the project folder.
2. Open the folder in your preferred IDE (e.g., **VS Code**).
3. Open the terminal inside your IDE and install the required dependencies:

bash
pip install ultralytics opencv-python
---
##📁 Project Structure
Plaintext
Road_Inspection_Project/
│
├── app.py                 # Core Python script for video processing & inference
├── best.pt                # Custom-trained YOLOv8 weights (The AI "Brain")
├── input.mp4              # Sample input video (Drone/Dashcam footage)
├── output_result.mp4      # Final processed video with bounding boxes & alerts
└── README.md              # Project documentation
---
##🕹️ How to Use
Place your target video in the main project folder and ensure it is named input.mp4 (or change the video_path variable inside app.py to match your video's name).

Run the application from your terminal:

Bash
python app.py
A live window will appear, showing the AI inspecting the road in real time.

Controls: Press the Q key to stop the process at any time.

Once the video finishes (or you press q), check your folder for the output_result.mp4 file to see the final saved results.

##📊 Model Training Details
The underlying object detection model was trained from scratch specifically for road damage.

Architecture: YOLOv8 (Ultralytics)

Training Environment: Google Colab (Tesla T4 GPU)

Dataset: Roboflow Universe (road-damage-det)

Epochs: 50

Image Size: 640x640

Data Augmentation: Applied random cropping, rotations, and brightness adjustments to simulate varying outdoor lighting and drone camera angles.
---

## 👨‍💻 Author & Contact

**Muhammad Mahad** *Computer Vision & AI Enthusiast*

If you have any questions, suggestions, or want to collaborate on this project, feel free to reach out:

* 📧 **Email:** [muhammadmahad.cs@gmail.com]
* 💼 **LinkedIn:** [https://www.linkedin.com/in/muhammadmahad-cs/]
* 🐙 **GitHub:** [@YourGitHubUsername](https://github.com/M-MAHAD1)

---
