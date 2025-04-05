"""
File: sensor_fusion_jetson.py
Description: Real-time GPS + camera data fusion and logging on Jetson Nano.
"""

import serial
import time
import cv2

# Connect to GPS via serial port
gps = serial.Serial("/dev/ttyUSB0", baudrate=9600)

# Open camera
cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    gps_data = gps.readline().decode('utf-8')
    timestamp = time.time()

    # Log to file
    with open("fused_log.txt", "a") as f:
        f.write(f"{timestamp},{gps_data.strip()}\n")

    cv2.imshow("Cam", frame)
    if cv2.waitKey(1) == ord('q'):
        break

