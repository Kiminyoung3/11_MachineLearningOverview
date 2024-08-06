import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000) #배열 내에 1000개의 랜덤한 수를 뽑는다.

plt.clf()

plt.hist(data, bins=20, color='LightPink', edgecolor='Green')

plt.title("Histogram Chart") #랜덤 수들의 빈도 파악
plt.xlabel("Values")
plt.ylabel("Frequency")

plt.savefig("./results_histogram.png")