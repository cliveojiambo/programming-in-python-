
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def main():

    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))

    primes = find_primes_in_range(start, end)

    if primes:
        print(f"Prime numbers between {start} and {end}: {primes}")
    else:
        print(f"There are no prime numbers between {start} and {end}.")

if __name__ == "__main__":
    main()

