#printing the numbers from 1 to N
#i = 1
#while i < 5: # condition
#   print(i)
#   i +=1 #increment
#n = int(input("Enter a value: "))
#for i in range(1,n+1):
#    print(i)

#sum of n numbers by using function
def cal_sum(n):
    total = 0
    for i in range(1,n+1):
        total += i 
    return total

def main():
    n = int(input("Enter a value: "))
    print(cal_sum(n))
main()