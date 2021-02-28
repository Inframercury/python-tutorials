def calculate_sqrt(input):
    low = 0
    high = input
    while low <= high:
        mid = low + (high - low) // 2
        if mid ** 2 == input:
            return mid
        elif mid ** 2 < input:
            low = mid + 1
        elif mid ** 2 > input:
            high = mid - 1
    return None

print(calculate_sqrt(3))


