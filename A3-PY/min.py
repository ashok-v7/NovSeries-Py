def find_minimum(nums):
    if not nums:  # Check if the list is empty
        return "The list is empty"

    min_val = nums[0]
    for num in nums:
        if num < min_val:
            min_val = num
    return min_val


def find_maximum(nums):
    if not nums:  # Check if the list is empty
        return "The list is empty"
    max_val = nums[0]
    for num in nums:
        if num > max_val:
            max_val = num
    return max_val


# Example usage
nums = [3, 6, 8, 2]
min_result = find_minimum(nums)
max_result = find_maximum(nums)
print("min_result", min_result)
print("max_result", max_result)
