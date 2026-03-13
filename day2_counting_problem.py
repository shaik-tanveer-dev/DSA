# #count even from 1 to n
# def count_even(n):
#     count = 0
#     for i in range(1,n+1):
#         if i %2 ==0:
#             count += 1
#     return count

# def main():
#     n =int(input("Enter a value : "))
#     print("Even count: ",count_even(n))

# main()

#count digits in a given number

def count_digits(num):
    count=0
    while num>0:
        num = num // 10
        count += 1
    return count

def main():
    num =int(input("Enter a value: "))
    print("Number of digits in a given number:",count_digits(num))

main()