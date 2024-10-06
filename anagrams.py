

def are_anagrams(str1, str2):
    # Remove any spaces and convert both strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    return sorted(str1) == sorted(str2)

def main():

    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")
   
    if are_anagrams(string1, string2):
        print(f'"{string1}" and "{string2}" are anagrams.')
    else:
        print(f'"{string1}" and "{string2}" are not anagrams.')

if __name__ == "__main__":
    main()
