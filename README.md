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

/code/ → All Python code scripts
/models/ → Trained models (YOLOv8, GRU)
/data/ → Sample GPS logs and escape simulations
/results/ → Output charts and graphs
/docs/ → Flowcharts and system diagrams


---

## 📊 Visual Output Examples

- Graphs: Jerk, EscapeScore over time
- Bar Chart: Accuracy by lighting condition
- Pie Chart: Escape behavior breakdown
- Flowchart: Full real-time system architecture

---

## 🔧 Setup Instructions

1. Clone this repo
2. Run `pip install -r requirements.txt`
3. Execute each script from `/code/` to reproduce results

For Jetson Nano deployment, see `sensor_fusion_jetson.py`

---

## 📂 Supplementary Material

All visuals and implementation scripts used in the paper are here.  
This GitHub repo is referenced in the paper’s abstract and methodology section.

📎 **Citation:**  
> *"The implementation code and demonstration videos are available at: [https://github.com/Paras-Vermaa/SmartTruck-HitAndRun-Detection-]"*

---

## 📜 License

MIT License – Free for academic, research, and non-commercial use.

---

Let me know once your files are uploaded—I can review or help polish anything, including the README.  
Standing by for next command, Commander. 🫡
