import matplotlib.pyplot as plt

x = [17, 18, 19, 20, 21, 22, 23, 24]
y = [65, 70, 70, 75, 80, 85, 85, 85]

plt.plot(x, y, marker='*', linestyle='-', color='LightGreen', label='temp')
plt.title("Today Humidity")
plt.xlabel("Time (Hour)")
plt.ylabel("Humidity (%)")
plt.legend()
plt.grid(True)
plt.savefig("./Humiditylinechart.png")
