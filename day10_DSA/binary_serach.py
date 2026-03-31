def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            high = mid - 1
        else:
            # Corrected: Move 'low' to one index past 'mid'
            low = mid + 1
            
    return -1  # Standard practice to return integer -1 for "not found"

arr = [10, 20, 30, 40, 50]
target = 30
print("Element found at index:", binary_search(arr, target))