
import matplotlib.pyplot as plt
import numpy as np

# ENTER TIME VALUES (seconds)

time = [0,30,60,90,120,150,180,210,240,270,300,330,360,390,420,450,480,510,540,570,600,630,660,690,720,750,780,810,840,870,900,930,960,990,1020,1050,1080,1110,1140,1170,1200]


# ENTER SPEED VALUES (km/h)

speed_kmh = [0,50,44,23,43,49,46,43,16,50,52,53,24,15,33,40,22,38,60,60,34,6,33,54,35,48,51,64,67,63,66,60,67,31,31,8,45,60,56,12,0]


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



