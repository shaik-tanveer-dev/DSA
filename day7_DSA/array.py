# #counting elements in the array
# def count_array(arr):
#     count = 0
#     for i in arr:
#         count += 1
#     return count

# # arr = [1,9,8,7,6,5]
# # print(count_array(arr))/

#counting the even number in the array

# def count_even(arr):
#     count = 0
#     for i in arr:
#         if i % 2==0:
#             count += 1
#     return count

# arr = [1,2,5,6,4,4,6]
# print(count_even(arr))

#finding the maxminum value in arr

def max_value(arr):
    max[0] = 0
    for i in arr:
        if i > max[0]:
             i+=1
    return max[i]

arr = [13,56,43,56,5]
print(max_value(arr))