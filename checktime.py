import random
import timeit
import sortFunc
import matplotlib.pyplot as plt


small_arr = [random.randint(1, 1000) for _ in range(100)]
middle_arr = [random.randint(1, 1000) for _ in range(1000)]
large_arr = [random.randint(1, 1000) for _ in range(10000)]

ts_insertion = timeit.timeit(lambda: sortFunc.insertion_sort(small_arr), number = 10)
ts_merge = timeit.timeit(lambda: sortFunc.merge_sort(small_arr), number = 10)
ts_sort = timeit.timeit(lambda: sortFunc.timesort_and_return(small_arr), number = 10)
ts_sorted = timeit.timeit(lambda: sortFunc.timesorted_and_return(small_arr), number = 10)

tm_insertion = timeit.timeit(lambda: sortFunc.insertion_sort(middle_arr), number = 10)
tm_merge = timeit.timeit(lambda: sortFunc.merge_sort(middle_arr), number = 10)
tm_sort = timeit.timeit(lambda: sortFunc.timesort_and_return(middle_arr), number = 10)
tm_sorted = timeit.timeit(lambda: sortFunc.timesorted_and_return(middle_arr), number = 10)

tl_insertion = timeit.timeit(lambda: sortFunc.insertion_sort(large_arr), number = 10)
tl_merge = timeit.timeit(lambda: sortFunc.merge_sort(large_arr), number = 10)
tl_sort = timeit.timeit(lambda: sortFunc.timesort_and_return(large_arr), number = 10)
tl_sorted = timeit.timeit(lambda: sortFunc.timesorted_and_return(large_arr), number = 10)


print (f"|{'Algorithm':<20} | {'Small':<20} | {'Middle':<20} | {'Large':<20} |")
print (f"|{'-'*20} | {'-'*20} | {'-'*20} | {'-'*20} |")
print (f"|{'Insertion sort':<20} | {ts_insertion:20.5f} | {tm_insertion:20.5f} | {tl_insertion:20.5f} |")
print (f"|{'Merge sort':<20} | {ts_merge:20.5f} | {tm_merge:20.5f} | {tl_merge:20.5f} |")
print (f"|{'Sort':<20} | {ts_sort:20.5f} | {tm_sort:20.5f} | {tl_sort:20.5f} |")
print (f"|{'Sorted':<20} | {ts_sorted:20.5f} | {tm_sorted:20.5f} | {tl_sorted:20.5f} |")

