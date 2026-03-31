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
- [Future Enhancements](#-future-enhancements)

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
1. **Data Ingestion:** Video footage (`test_video.mp4`) is loaded using OpenCV.
2. **Inference Engine:** Each frame is passed through the custom YOLOv8 model (`best.pt`).
3. **Logic & Annotation:** Bounding boxes are drawn around detected defects. A logic gate checks the defect count to assign a "Status" to the frame.
4. **Output Generation:** The processed frame is displayed live and simultaneously written to an output video file (`output_result.mp4`).

---

## 📁 Project Structure

```text
Road_Inspection_Project/
│
├── app.py                 # Core Python script for video processing & inference
├── best.pt                # Custom-trained YOLOv8 weights (The AI "Brain")
├── test_video.mp4         # Sample input video (Drone/Dashcam footage)
├── output_result.mp4      # Final processed video with bounding boxes & alerts
└── README.md              # Project documentation
