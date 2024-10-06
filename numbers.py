def sum_of_list(numbers):
    return sum(numbers)


def main():
   
    numbers = list(map(float, input("Enter a list of numbers separated by spaces: ").split()))

    total = sum_of_list(numbers)
 
    print(f"The sum of the list is: {total:.2f}")


if __name__ == "__main__":
    main()
