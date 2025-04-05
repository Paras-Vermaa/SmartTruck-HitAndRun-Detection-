"""
File: plot_escape_metrics.py
Description: Plots Jerk and EscapeScore metrics over time using matplotlib.
"""

import matplotlib.pyplot as plt

# Simulated data
time = [0, 1, 2, 3, 4, 5, 6, 7, 8]
jerk = [0.1, 1.2, 6.3, 3.0, 1.5, 0.5, 0.2, 0.1, 0.0]
escape_score = [0.82, 0.85, 0.79, 0.87, 0.80, 0.91, 0.89, 0.84, 0.80]

# Plot Jerk
plt.plot(time, jerk, marker='o', label='Jerk (m/s³)')
plt.axhline(6, color='r', linestyle='--', label='Jerk Threshold (6 m/s³)')
plt.xlabel("Time (s)")
plt.ylabel("Jerk")
plt.title("Graph 1: Jerk Over Time")
plt.legend()
plt.grid(True)
plt.show()

# Plot EscapeScore
plt.plot(time[1:], escape_score, marker='o', color='blue', label='EscapeScore')
plt.axhline(0.8, color='r', linestyle='--', label='Threshold (0.8)')
plt.xlabel("Time (s)")
plt.ylabel("EscapeScore")
plt.title("Graph 2: EscapeScore Over Time")
plt.legend()
plt.grid(True)
plt.show()

