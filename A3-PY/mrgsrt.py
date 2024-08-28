'''
Fast: Merge sort is much faster than bubble sort, being O(n*log(n)) instead of O(n^2).
Stable: Merge sort is also a stable sort which means that values with duplicate keys in the original list will be 
in the same order in the sorted list.
Extra memory: Most sorting algorithms can be performed using a single copy of the original array. 
Merge sort requires an extra array in memory to merge the sorted subarrays.
Recursive: Merge sort requires many recursive function calls, and function calls can have significant resource overhead.

The algorithm consists of two separate functions, merge_sort and merge.

merge_sort() divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves.
The merge() function is used for merging two sorted lists back into a single sorted list. At the lowest level of recursion, the two "sorted" lists will each have a length of 1. Those single element lists will be merged into a sorted list of length two, and we can build from there.

MERGE_SORT() IMPLEMENTATION
Input: A, a list of integers

If the length of A is less than 2, it's already sorted so return it
Split the input array into two halves down the middle
Call merge_sort() twice, once on each half
Return the result of calling merge(sorted_left_side, sorted_right_side) on the results of the merge_sort() calls
MERGE() IMPLEMENTATION
Inputs: A, B. Two lists of integers

Create a new "final" list of integers.
Set i and j equal to zero. They will be used to keep track of indexes in the input lists (A and B).
Use a loop to iterate over A and B at the same time. If an element in A is less than or equal to its respective element 
in B, add it to the final list and increment i. Otherwise, add the item in B to the final list and increment j.
After comparing all the items, there may be some items left over in either A or B (if one of the lists is longer 
than the other). Add those extra items to the final list.
Return the final list.

'''


def merge_sort(nums):
    if len(nums) < 2:
        return nums
    first = merge_sort(nums[: len(nums) // 2])
    second = merge_sort(nums[len(nums) // 2:])
    return merge(first, second)


def merge(first, second):
    final = []
    i = 0
    j = 0
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1
    while i < len(first):
        final.append(first[i])
        i += 1
    while j < len(second):
        final.append(second[j])
        j += 1
    return final


nums = [64, 34, 25, 12, 22, 11, 90]
sorted_nums = merge_sort(nums)
print("Sorted numbers:", sorted_nums)
