# def first_occurence(arr, target):
#     low = 0
#     high = len(arr) - 1
#     result = -1

#     while low <= high:
#         mid = (low + high) // 2

#         if arr[mid] == target:
#             result = mid       # store result
#             high = mid - 1     # move left to find first occurrence
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1

#     return result

# arr = [1, 2, 2, 2, 3, 4]
# target = 3
# print(first_occurence(arr, target))  

def search_rotated_arr(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        # Left part is sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

        # Right part is sorted
        else:
            if arr[mid] <= target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1   
    
arr = [4,5,6,7,8,2,1]
target = 6
print("Index:", search_rotated_arr(arr, target))