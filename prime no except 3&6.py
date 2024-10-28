Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. 

Note : Use 'continue' statement. 

Expected Output : 0 1 2 4 5


for number in range(7):
    if number == 3 or number == 6:
        continue  # Skip the rest of the loop for 3 and 6
    print(number, end=' ')  # Print the number with a space
