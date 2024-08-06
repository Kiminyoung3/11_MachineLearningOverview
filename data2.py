import matplotlib.pyplot as plt

categories = ["Apple", "Banana", "Orange", "strawberry", "Grape"]
values = [25, 30, 15, 20, 35]

plt.clf()

plt.bar(categories, values, color='SkyBlue')

plt.title("Fruit Sales")

plt.xlabel("Fruit")
plt.ylabel("Sales")

plt.savefig("./results_bar_chart.png")

