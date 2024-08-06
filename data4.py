import matplotlib.pyplot as plt

labels = ['English', "Math", "Science", "History"]
sizes = [45, 30, 15, 10]

plt.clf()

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=["LightBlue", "LightPink", "LightGreen", "Lightcoral"])

plt.title("Subjects Distribution")
plt.savefig("./results_chart")