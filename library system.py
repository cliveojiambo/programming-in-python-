
from datetime import datetime

def calculate_fine(days_overdue):
    if days_overdue <= 7:
        fine_rate = 20
    elif 8 <= days_overdue <= 14:
        fine_rate = 50
    else:
        fine_rate = 100

    fine_amount = fine_rate * days_overdue
    return fine_rate, fine_amount



def convert_date(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d')



def main():

    book_id = input("Enter the Book ID: ")
    due_date_str = input("Enter the Due Date (YYYY-MM-DD): ")
    return_date_str = input("Enter the Return Date (YYYY-MM-DD): ")


    due_date = convert_date(due_date_str)
    return_date = convert_date(return_date_str)


    days_overdue = (return_date - due_date).days


    if days_overdue > 0:
        fine_rate, fine_amount = calculate_fine(days_overdue)
    else:
        fine_rate = 0
        fine_amount = 0
        days_overdue = 0  # No overdue


    print("\n--- Library Fine Details ---")
    print(f"Book ID: {book_id}")
    print(f"Due Date: {due_date_str}")
    print(f"Return Date: {return_date_str}")
    print(f"Days Overdue: {days_overdue} days")
    print(f"Fine Rate: Ksh {fine_rate} per day")
    print(f"Total Fine Amount: Ksh {fine_amount}")

if __name__ == "__main__":
    main()
