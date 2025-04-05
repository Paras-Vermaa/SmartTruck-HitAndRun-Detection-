"""
File: escape_score.py
Description: Computes EscapeScore using jerk, speed change, route deviation, and frame exit time.
Extracted from research paper: 'SmartTruck Hit-and-Run Detection Framework'
"""

def calculate_escape_score(jerk, speed_change, route_dev, time_to_exit):
    w1, w2, w3, w4 = 0.3, 0.3, 0.2, 0.2  # Tuned weights
    score = (w1 * jerk) + (w2 * speed_change) + (w3 * route_dev) + (w4 * time_to_exit)
    return score

# Example use-case
score = calculate_escape_score(jerk=2.5, speed_change=12.3, route_dev=0.04, time_to_exit=1.8)
if score > 1.5:
    print("Hit-and-Run Detected!")

