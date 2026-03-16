# fee calculator

def calculate_fee(course, marks):
    if course == "AI":
        fee = 50000
    elif course == "web":
        fee =30000
    elif course == "data science":
        fee = 40000
    else:
        return None 
    
    if marks > 90:
        fee -= 5000
    return fee

def main():
    course = input("Enter course name: ")
    marks = int(input("Enter marks: "))

    fee = calculate_fee(course,marks)

    if fee is None:
        print("Invalid course selected")
    else:
        print("final fee:   ",fee)

main()