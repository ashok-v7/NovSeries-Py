'''
Procedure bubble_sort(nums):
    Set swapping to True
    Set end to the length of nums
    While swapping is True:
        Set swapping to False
        For i from the 2nd element to end:
            If the (i-1)th element of nums is greater than the ith element:
                Swap the (i-1)th element and the ith element of nums
                Set swapping to True
        Reduce end by one
    Return nums
End Procedure

Bubble sort is famous for how easy it is to write. It's one of the slowest sorting algorithms, 
but can be useful for a quick script or when the amount of data to be sorted is guaranteed to be small
'''


def bubble_sort(nums):
    swapping = True
   # end = len(nums)
    while swapping:
        swapping = False
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
                swapping = True
    #    end -= 1                       
    return nums


# Example usage:
nums = [64, 34, 25, 12, 22, 11, 90]
sorted_nums = bubble_sort(nums)
print("Sorted numbers:", sorted_nums)
