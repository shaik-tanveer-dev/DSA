#function to check prime number
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
        
    return True

def main():
    num  = int(input("Enter number: "))
    if is_prime(num):
        print("Prime")
    else:
        print("Not Prime")

main()