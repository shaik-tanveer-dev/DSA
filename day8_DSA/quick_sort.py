def quickselect(arr, k):
    return helper(arr, 0, len(arr) - 1, k - 1)

def helper(arr, low, high, k):
    if low <= high:
        pivot_index = partition(arr, low, high)

        if pivot_index == k:
            return arr[pivot_index]
        elif pivot_index > k:
            return helper(arr, low, pivot_index - 1, k)
        else:
            return helper(arr, pivot_index + 1, high, k)

def partition(arr, low, high):
    pivot = arr[high]
    i = low

    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[high] = arr[high], arr[i]
    return i

# Example
arr = [7, 10, 4, 3, 20, 15]
k = 3

result = quickselect(arr, k)

print("Array:", arr)
print(f"{k}th smallest element is:", result)