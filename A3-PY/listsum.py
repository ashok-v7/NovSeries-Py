def sum(nums):
    result = 0
    for num in nums:
        result += num
    return result


def average_followers(nums):
    if len(nums) == 0:
        return None
    sum = 0
    for num in nums:
        sum += num
    return sum / len(nums)


def median_followers(nums):
    nums.sort()
    n = len(nums)
    mid_index = n // 2
    if n % 2 == 1:
        median = nums[mid_index]
    else:
        median = (nums[mid_index-1] + nums[mid_index]) / 2
    return median


# Example usage
nums = [3, 6, 8, 2, 7, 9, 1]
result = sum(nums)
avg = average_followers(nums)
median = median_followers(nums)
print("result:", result)
print("avg: ", avg)
print("median: ", median)
