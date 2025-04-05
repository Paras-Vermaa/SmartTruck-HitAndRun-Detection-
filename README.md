# SmartTruck-HitAndRun-Detection-

# SmartTruck-HitAndRun-Detection

🚚 A Real-Time AI-Based Surveillance Framework for Post-Accident Truck Behavior Analysis  
📍 Developed for research on hit-and-run detection using computer vision + telemetry.

## 🔍 Overview
This repository contains the codebase, model files, data samples, and visualization outputs from the research paper:
**"Data-Driven Detection of Hit-and-Run Truck Incidents Using Computer Vision and Telemetry"**

The system detects crash events, analyzes escape behavior (speed surge, route deviation, etc.), and confirms vehicle identity using YOLOv8 + LPR on Jetson Nano edge hardware.

---

## 🧠 System Modules

### 📷 Vision Module
- YOLOv8-based vehicle detection
- Tesseract OCR for license plates
- Escape trigger via IoU & DeepSORT tracking

### 📡 Telemetry Module
- GPS + Accelerometer (Jerk detection)
- Route deviation analysis via GRU model
- EscapeScore calculation logic

---

## 📁 Repository Structure

