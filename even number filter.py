def filter_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

def main():
   
    user_input = input("Enter a list of integers separated by spaces: ")
    numbers = list(map(int, user_input.split()))
    
    even_numbers = filter_even_numbers(numbers)
    
    print(f"The even numbers are: {even_numbers}")

if __name__ == "__main__":
    main()
