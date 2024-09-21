discount.py
C:\Users\user\PycharmProjects\programming in python\pythonProject\discount.py
amount = float(input("Enter the amount of purchase in Ksh: "))
if amount > 1000:
    discount = 0.05 * amount
    total = amount - discount
    print(f"A discount of Ksh {discount:.2f} has been applied.")
else:
    total = amount
    print("No discount applied.")

print(f"Total amount to pay: Ksh {total:.2f}")
