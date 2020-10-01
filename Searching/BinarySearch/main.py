import random
import matplotlib.pyplot as plt
from binary_search import binary_search
from timeit import default_timer as timer

data_size = list()
best_case = list()
worst_case = list()


for i in range(1000, 100001, 500):
    data = random.sample(range(100000), i)
    data.sort()
    data_size.append(i)

    start_time_worst = timer()
    binary_search(data, 0, i-1, data[-1])
    worst_case.append(timer() - start_time_worst)

    start_time_best = timer()
    mid = data[(i-1) // 2]
    binary_search(data, 0, i-1, mid)
    best_case.append(timer() - start_time_best)


plt.plot(data_size, best_case, 'g', label="Best Case")
plt.plot(data_size, worst_case, 'r', label="Worst Case")
plt.xlabel("Data Size")
plt.ylabel("Time Taken")
plt.title("Best and Worst case Time Complexity of Binary Search")
plt.legend()
plt.savefig('Binary Search.png', dpi=300, format='png', pad_inches=1.0)
plt.show()
