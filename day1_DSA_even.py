# def even(n):
#     if n%2==0:
#         return 'even'
#     else:
#         return 'odd'

# def main():
#     n = int(input("Enetr a value: "))
#     print("Number is : ",even(n))

# main()

def even_num(n):
    count = 0
    for i in range(1,n+1):
        if i % 2 ==0:
            print(i)
            count +=1
    return count
    
def main():
    n = int(input("Enter a value: "))
    print("Even numbers: ",even_num(n))

main()