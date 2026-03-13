def counting_char(string):
    count = 0
    for ch in string:
        count += 1
    return count

def main():
    string = input("Enter your text: ")
    print(counting_char(string))

main()
