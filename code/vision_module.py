"""
File: vision_module.py
Description: Detects trucks using YOLOv8 and extracts license plate using Tesseract OCR.
"""

from ultralytics import YOLO
import pytesseract
import cv2

# Load model
model = YOLO("yolov8n.pt")  # Or path to custom weights

# Inference on a sample frame
frame = cv2.imread("frame.jpg")
results = model(frame)

# Extract license plate region
for box in results.boxes:
    if box.cls == "truck":  # Assumes class label mapping
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        plate_img = frame[y1:y2, x1:x2]

        # OCR
        gray = cv2.cvtColor(plate_img, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray, config='--psm 8')
        print("License Plate:", text)

