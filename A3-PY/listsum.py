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


# Example usage
nums = [3, 6, 8, 2]
result = sum(nums)
avg = average_followers(nums)
print("result:", result)
print("avg: ", avg)
