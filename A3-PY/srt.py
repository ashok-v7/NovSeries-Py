def sort(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                # Swap the elements
                nums[i], nums[j] = nums[j], nums[i]
    return nums


# Example usage
nums = [3, 6, 8, 2]
result = sort(nums)
print(result)  # [2, 3, 6, 8]
