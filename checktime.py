import random
import timeit
import sortFunc
import matplotlib.pyplot as plt

def sorting_times(arr):

    sorting_times_insertion = []
    sorting_times_merge = []
    sorting_times_sort = []
    sorting_times_sorted = []

    for size in arr:
        arr = list(range(size))

        ts_insertion = timeit.timeit(lambda: sortFunc.insertion_sort(arr), number = 10)
        ts_merge = timeit.timeit(lambda: sortFunc.merge_sort(arr), number = 10)
        ts_sort = timeit.timeit(lambda: sortFunc.timesort_and_return(arr), number = 10)
        ts_sorted = timeit.timeit(lambda: sortFunc.timesorted_and_return(arr), number = 10)

        sorting_times_insertion.append(ts_insertion)
        sorting_times_merge.append(ts_merge)
        sorting_times_sort.append(ts_sort)
        sorting_times_sorted.append(ts_sorted)

    return ts_insertion, ts_merge, ts_sort, ts_sorted, sorting_times_insertion, sorting_times_merge, sorting_times_sort, sorting_times_sorted


small_arr = [random.randint(1, 1000) for _ in range(100)]
middle_arr = [random.randint(1, 1000) for _ in range(1000)]
large_arr = [random.randint(1, 1000) for _ in range(10000)]

sorting_resultsS = sorting_times(small_arr)
sorting_resultsM = sorting_times(middle_arr)
sorting_resultsL = sorting_times(large_arr)

print (f"|{'Algorithm':<20} | {'Small':<20} | {'Middle':<20} | {'Large':<20} |")
print (f"|{'-'*20} | {'-'*20} | {'-'*20} | {'-'*20} |")
print (f"|{'Insertion sort':<20} | {sorting_resultsS[0]:20.5f} | {sorting_resultsM[0]:20.5f} | {sorting_resultsL[0]:20.5f} |")
print (f"|{'Merge sort':<20} | {sorting_resultsS[1]:20.5f} | {sorting_resultsM[1]:20.5f} | {sorting_resultsL[1]:20.5f} |")
print (f"|{'Sort':<20} | {sorting_resultsS[2]:20.5f} | {sorting_resultsM[2]:20.5f} | {sorting_resultsL[2]:20.5f} |")
print (f"|{'Sorted':<20} | {sorting_resultsS[3]:20.5f} | {sorting_resultsM[3]:20.5f} | {sorting_resultsL[3]:20.5f} |")

# Виведення графіків
plt.figure(figsize=(10, 5))
plt.plot(small_arr, sorting_resultsS[4], label='Insertion Sort')
plt.plot(small_arr, sorting_resultsS[5], label='Merge Sort')
plt.plot(small_arr, sorting_resultsS[6], label='Sort')
plt.plot(small_arr, sorting_resultsS[7], label='Sorted')
plt.xlabel('List size Small')
plt.ylabel('Run time (seconds)')
plt.title('Sorting speed')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(large_arr, sorting_resultsL[4], label='Insertion Sort')
plt.plot(large_arr, sorting_resultsL[5], label='Merge Sort')
plt.plot(large_arr, sorting_resultsL[6], label='Sort')
plt.plot(large_arr, sorting_resultsL[7], label='Sorted')
plt.xlabel('List size Middle')
plt.ylabel('Run time (seconds)')
plt.title('Sorting speed')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(middle_arr, sorting_resultsM[4], label='Insertion Sort')
plt.plot(middle_arr, sorting_resultsM[5], label='Merge Sort')
plt.plot(middle_arr, sorting_resultsM[6], label='Sort')
plt.plot(middle_arr, sorting_resultsM[7], label='Sorted')
plt.xlabel('List size Large')
plt.ylabel('Run time (seconds)')
plt.title('Sorting speed')
plt.legend()
plt.grid(True)
plt.show()

