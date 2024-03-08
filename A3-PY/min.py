def find_minimum(nums):
    minimum = float("inf")
    print(minimum)
    if not nums:  # Check if the list is empty
        return "The list is empty"

    min_val = nums[0]
    for num in nums:
        if num < min_val:
            min_val = num
    return min_val


# Example usage
nums = [3, 6, 8, 2]
result = find_minimum(nums)
print(result)
