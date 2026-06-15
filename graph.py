
import matplotlib.pyplot as plt
import numpy as np

# ENTER TIME VALUES (seconds)

time = [0, 60, 120, 180, 240, 300, 360, 420, 480, 540, 600, 660, 720, 780, 840, 900, 960, 1020, 1080, 1140, 1200]


# ENTER SPEED VALUES (km/h)

speed_kmh = [0, 48, 43, 51, 18, 50, 28, 33, 21, 62, 34, 32, 36, 52, 68, 67, 67, 39, 49, 20, 0]


# ACTUAL DISTANCE FROM GOOGLE MAPS
# 16 km = 16000 meters


actual_distance = 16000

# CONVERT km/h TO m/s

speed_ms = []

for s in speed_kmh:
    speed_ms.append(s * 5 / 18)

# CALCULATE DISTANCE USING GRAPH

distance = np.trapezoid(speed_ms, time)
# PERCENTAGE ERROR

percentage_error = abs(distance - actual_distance) / actual_distance * 100

# RESULTS

print("\n========== RESULTS ==========")

print(f"Distance from Graph = {distance:.2f} meters")

print(f"Actual Distance     = {actual_distance:.2f} meters")

print(f"Percentage Error    = {percentage_error:.2f} %")

# PLOT GRAPH

plt.figure(figsize=(10,5))

plt.plot(time, speed_ms, marker='o')

plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Velocity vs Time Graph")

plt.grid(True)

# Save graph image
plt.savefig("velocity_graph.png", dpi=300)

print("\nGraph saved as velocity_graph.png")

plt.show()



