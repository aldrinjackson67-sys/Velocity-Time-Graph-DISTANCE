
import matplotlib.pyplot as plt
import numpy as np

# ==========================================
# ENTER TIME VALUES (seconds)
# ==========================================

time = [0, 120, 240, 360, 480, 600, 720, 840, 960, 1080, 1200]

# ==========================================
# ENTER SPEED VALUES (km/h)
# Must match time values
# ==========================================

speed_kmh = [0, 40, 18, 25, 21, 34, 36, 68, 67, 49, 0]

# ==========================================
# ACTUAL DISTANCE FROM GOOGLE MAPS
# 16 km = 16000 meters
# ==========================================

actual_distance = 16000

# ==========================================
# CONVERT km/h TO m/s
# ==========================================

speed_ms = []

for s in speed_kmh:
    speed_ms.append(s * 5 / 18)

# ==========================================
# CALCULATE DISTANCE USING GRAPH
# ==========================================

distance = np.trapezoid(speed_ms, time)
# ==========================================
# PERCENTAGE ERROR
# ==========================================

percentage_error = abs(distance - actual_distance) / actual_distance * 100

# ==========================================
# RESULTS
# ==========================================

print("\n========== RESULTS ==========")

print(f"Distance from Graph = {distance:.2f} meters")

print(f"Actual Distance     = {actual_distance:.2f} meters")

print(f"Percentage Error    = {percentage_error:.2f} %")

# ==========================================
# PLOT GRAPH
# ==========================================

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



