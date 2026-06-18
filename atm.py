pin = "1234"
balance = 10000
enter_pin = input("Enter your bank pin: ")
while enter_pin != "1234": 
    print("Access Denied, Try again!")
    enter_pin = input("Enter your bank pin: ")

while enter_pin == "1234":
    print("Access Accepted!")
    print()
    print("Option 1: Check Balance")
    print("Option 2: Withdraw Money")
    print("Option 3: Deposit Money")
    print("Option 4: Exit")
    choice = float(input("Select an option: "))

    while choice == 1:
        print(f"Your current balance is Rs. {balance}")
        print()
        choice = float(input("Select an option: "))

    while choice == 2: 
        withdraw = float(input("Enter amount you want to withdraw: "))
        balance = balance-withdraw
        print(f"Your remaining balance is Rs. {balance}")
        print()
        choice = float(input("Select an option: "))

    while choice == 3: 
        deposit = float(input("Enter amount you want to deposit: "))
        balance = balance+deposit
        print(f"Your new balance is Rs. {balance}")
        print()
        choice = float(input("Select an option: "))

    while choice == 4: 
        print("Thank you for using the ATM!")
        break
    break
