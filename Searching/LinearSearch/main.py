import random
import matplotlib.pyplot as plt
from linear_search import linear_search
from timeit import default_timer as timer

data_size = list()
best_case = list()
worst_case = list()

for i in range(1000, 100001, 500):
    data = random.sample(range(100000), i)
    data_size.append(i)

    start_time_worst = timer()
    linear_search(data, data[-1])
    worst_case.append(timer() - start_time_worst)

    start_time_best = timer()
    linear_search(data, data[0])
    best_case.append(timer() - start_time_best)


plt.plot(data_size, best_case, 'g', label="Best Case")
plt.plot(data_size, worst_case, 'r', label="Worst Case")
plt.xlabel("Data Size")
plt.ylabel("Time Taken")
plt.title("Best and Worst case Time Complexity of Linear Search")
plt.legend()
plt.savefig('Linear Search.png', dpi=300, format='png', pad_inches=1.0)
plt.show()
