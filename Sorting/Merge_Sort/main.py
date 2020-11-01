import random
import matplotlib.pyplot as plt
from merge_sort import merge_sort
from timeit import default_timer as timer

data_size = list()
time_taken = list()

for i in range(1000, 100001, 500):
    data = random.sample(range(100000), i)
    data_size.append(i)
    start_time = timer()
    merge_sort(data)
    time_taken.append(timer() - start_time)


plt.plot(data_size, time_taken, 'g')
plt.xlabel("Data Size")
plt.ylabel("Time Taken")
plt.title("Time Complexity of Merge Sort")
plt.savefig('Merge Sort.png', dpi=300, format='png', pad_inches=1.0)
plt.show()
