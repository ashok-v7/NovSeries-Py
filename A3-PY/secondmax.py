def find_max_and_second_max(arr):
    if len(arr) < 2:
        return "Array does not have enough elements", "Array does not have enough elements"

    nmax = max(arr[0], arr[1])
    n2max = min(arr[0], arr[1])

    for num in arr[2:]:
        if num > nmax:
            n2max = nmax
            nmax = num
        elif n2max < num < nmax:
            n2max = num

    return nmax, n2max


# Example usage
arr = [3, 5, 2, 7]
nmax, n2max = find_max_and_second_max(arr)
print(nmax)   # 7
print(n2max)  # 5
