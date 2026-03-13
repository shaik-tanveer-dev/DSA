def reverse_string(string):
    rev = ""
    for ch in string:
        rev = ch + rev
    return rev

def main():
    tex = input("Enter a string: ")
    print(reverse_string(tex))

main()