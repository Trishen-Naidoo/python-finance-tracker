#Global variable to store the balance in every function
Balance=0

#Function to add income
def income():
    global Balance
    income_amount = float(input("Enter your income amount: "))       
    Balance += income_amount
    print(f"Income of {income_amount} added. New balance is: {Balance}")

#Function to add expense
def expense():
    global Balance
    expense_amount = float(input("Enter your expense amount: "))
    if expense_amount > Balance:
        print("Insufficient balance for this expense.")
    else:
        Balance -= expense_amount
        print(f"Expense of {expense_amount} deducted. New balance is: {Balance}")

#Function to view the current balance
def view_balance():
    print(f"Your current balance is: {Balance}")

    




#User interface for the program
print("===========================")
print("      FINANCE TRACKER      ")
print("===========================")

#Entering the program

print("want to track your income and expenses? (y/n)")
choice_1 = str(input("Choice: "))

#Using While loop to catch invalid input and ask the user to enter a valid input
while choice_1 != "y" and choice_1 != "n":
    print("Invalid input. Please enter 'y' to continue or 'n' to exit.")
    choice_1 = str(input("Choice: "))
    if choice_1 == "n":
        print("Exiting the program.")
        exit()


#Choice list
print("Enter your choice number:")
print("1. Add Income")
print("2. Add Expense")
print("3. View Balance")
print("4. Exit")

#Program loop
#Using a while loop to keep the program running until the user exits
while choice_1 == "y":
    choice_2 = int(input("What do you want to do? Choose a number: "))
    try:
        if choice_2 == 1:
            income()
        elif choice_2 == 2:
            expense()
        elif choice_2 == 3:
            view_balance()
        elif choice_2 == 4:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
    except ValueError:
        print("Invalid input. Please enter a number.")

 


