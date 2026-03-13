def counting_char_vowels(string):
      count = 0
      vowel = "aeiouAEIOU"
      for ch in string:
            if ch in vowel:
                 count += 1
      return count

def main():
    string = input("Enter your text: ")
    print(counting_char_vowels(string))

main()
