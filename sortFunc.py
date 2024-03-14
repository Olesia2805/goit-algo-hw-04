# merge sort
import sortedcontainers

# insertion sort
import bisect

# the Timsort algorithm is already implemented in the built-in library,
# so it can be used without additional import

# insertion sort
def insertion_sort(arr):
    insertion_arr = []
    for num in arr:
        bisect.insort(insertion_arr, num)
    return insertion_arr

# merge sort
def merge_sort(arr):
    merge_arr = sortedcontainers.SortedList(arr)
    return merge_arr

# timsort (sort) -> change array and return None
def timesort_and_return(arr):
    timesort_arr = sorted(arr.copy())
    return timesort_arr

# timsort (sorted) -> return new
def timesorted_and_return(arr):
    timesorted_arr = sorted(arr)
    return timesorted_arr