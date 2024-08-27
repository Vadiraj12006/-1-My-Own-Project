import time
import random


def student_database():
    print("WELCOME TO STUDENT DATABASE")
    student = {
        'S001': {'name': 'Tarun', 'age': 20, 'major': 'Computer Science', 'password': 'Tarun@123',
                 'fees balance': 8000},
        'S002': {'name': 'Bob', 'age': 22, 'major': 'Mathematics', 'password': 'Bob@123', 'fees balance': 5000},
        'S003': {'name': 'Charlie', 'age': 21, 'major': 'Physics', 'password': 'Charlie@123', 'fees balance': 4100},
        'S004': {'name': 'Sindhu', 'age': 25, 'major': 'Chemistry', 'password': 'Sindhu@123', 'fees balance': 0}
    }

    studentid = input("Enter your Student ID: ")
    passw = input("Enter your Password: ")

    if studentid in student and student[studentid]['password'] == passw:
        print("Student Information:")
        print(f"Name: {student[studentid]['name']}")
        print(f"Age: {student[studentid]['age']}")
        print(f"Major: {student[studentid]['major']}")
        print(f"Balance Fees: {student[studentid]['fees balance']}")

        doyou = input("Do you want to pay your balance fees now (yes/no)? ")
        if doyou.lower() == "yes":
            if student[studentid]['fees balance'] > 0:
                try:
                    how = float(input("How much do you want to pay? "))
                    if how > 0:
                        if how <= student[studentid]['fees balance']:
                            student[studentid]['fees balance'] -= how
                            print(f"Payment successful. New balance: {student[studentid]['fees balance']}")
                        else:
                            print("Error: Payment exceeds balance.")
                    else:
                        print("Error: Invalid payment amount.")
                except ValueError:
                    print("Error: Please enter a valid number.")
            else:
                print("You have already paid your fees completely.")
    else:
        print("Invalid Credentials")


def print_with_delay(message, delay=1):
    print(message)
    time.sleep(delay)


def pucsim():
    print("Welcome to PUC Simulator")

    correct_answers = 0
    incorrect_answers = 0
    dumb = 0

    ask = input("Do you wish to enter?\n ")

    if ask.lower() == "yes":
        print_with_delay("Welcome to PUC Simulator - Where there is no escape -", 3)
        print_with_delay("Welcome to the First level...", 3)
        print_with_delay("Solve the below math to enter the next level:\n"
                         "3x + 5 = 20 and 2y - 7 = 15. Find the values of x and y.", 3)

        correct_x = 5
        correct_y = 11

        while True:
            try:
                x = int(input("Enter the value of x: "))
                y = int(input("Enter the value of y: "))
            except ValueError:
                print("Invalid input. Please enter numerical values.")
                incorrect_answers += 1
                dumb += 1
                continue

            if x == correct_x and y == correct_y:
                print_with_delay("Well done!\nYou passed level one. There's much more to go...", 2)
                print_with_delay("Welcome to the second level...\nThis is gonna be so much fun", 2)

                while True:
                    try:
                        bonds = int(input("How many bonds does C and O in aldehydes have?\n"))
                        formula = input("What is the chemical formula for METHANE?\n").strip().upper()
                        formula1 = input("What is the chemical formula for ETHYNE?\n").strip().upper()
                    except ValueError:
                        print("Invalid input. Please enter numerical values for bonds.")
                        incorrect_answers += 1
                        dumb += 1
                        continue

                    if bonds == 2 and formula == "CH4" and formula1 == "C2H2":
                        print_with_delay("Congratulations! You've completed the second level.", 2)
                        print_with_delay("This doesn't end here..\nGet ready for level 3", 2)

                        while True:
                            try:
                                eqn = input("What is the IDEAL GAS equation?\n").strip().upper()
                                const = float(input("What is the value of the Universal Gas Constant?\n").strip())
                                temp = float(
                                    input("What is the constant value to convert from Celsius to Kelvin?\n").strip())
                            except ValueError:
                                print("Invalid input. Please verify your answers.")
                                incorrect_answers += 1
                                dumb += 1
                                continue

                            if eqn == "PV=NRT" and const == 8.314 and temp == 273.15:
                                print_with_delay("Congratulations! You've completed the third level.", 2)
                                correct_answers += 1
                                break
                            else:
                                print("Some answers are incorrect. Try again.")
                                incorrect_answers += 1
                                dumb += 1

                        break
                    else:
                        print("Try again.")
                        incorrect_answers += 1
                        dumb += 1

                break
            else:
                print("Try again.")
                incorrect_answers += 1
                dumb += 1

        print("\nGame Over!")
        print(f"Total Correct Answers: {correct_answers}")
        print(f"Total Incorrect Answers: {incorrect_answers}")
        dumbness = correct_answers - dumb
        print(f"Dumbness calculator: {dumbness} IQ")

    else:
        print("You made the right decision - Goodbye!")


def calculator():
    print("WELCOME TO CALCULATOR")
    ch = input("Please choose the operation you want to perform\n"
               "1.ADDITION\n"
               "2.SUBTRACTION\n"
               "3.MULTIPLICATION\n"
               "4.DIVISION\n")
    if ch == "1":
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        sum = a + b
        print("The sum of two numbers = ", sum)
    elif ch == "2":
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        diff = a - b
        print("The difference between two numbers = ", diff)
    elif ch == "3":
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        product = a * b
        print("The product of two numbers = ", product)
    elif ch == "4":
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        if b == 0:
            print("Invalid operation")
        else:
            rem = a / b
            print("The result of division = ", rem)


def bank_database():
    print("WELCOME TO BANK DATABASE")
    print("Employees of our bank:")
    employees = ['Sindhu', 'Tarun', 'Ramesh', 'Guru', 'Abhishek', 'Aditya', 'Aman', 'Harish', 'Ram', 'Lakshman']
    for i in employees:
        print(i)
    import bcrypt

    # Example: User database with hashed passwords
    bank_users = {
        'Sindhu': {'password': bcrypt.hashpw('Sindhu$123'.encode(), bcrypt.gensalt()), 'name': 'Sindhu',
                   'account_balance': 60000},
        'Tarun': {'password': bcrypt.hashpw('Tarun$123'.encode(), bcrypt.gensalt()), 'name': 'Tarun',
                  'account_balance': 1500},
        'Ramesh': {'password': bcrypt.hashpw('Ramesh$123'.encode(), bcrypt.gensalt()), 'name': 'Ramesh',
                   'account_balance': 2000},
        'Guru': {'password': bcrypt.hashpw('Guru$123'.encode(), bcrypt.gensalt()), 'name': 'Guru',
                 'account_balance': 2500},
        'Abhishek': {'password': bcrypt.hashpw('Abhishek$123'.encode(), bcrypt.gensalt()), 'name': 'Abhishek',
                     'account_balance': 3000},
        'Aditya': {'password': bcrypt.hashpw('Aditya$123'.encode(), bcrypt.gensalt()), 'name': 'Aditya',
                   'account_balance': 3500},
        'Aman': {'password': bcrypt.hashpw('Aman$123'.encode(), bcrypt.gensalt()), 'name': 'Aman',
                 'account_balance': 4000},
        'Harish': {'password': bcrypt.hashpw('Harish$123'.encode(), bcrypt.gensalt()), 'name': 'Harish',
                   'account_balance': 4500},
        'Ram': {'password': bcrypt.hashpw('Ram$123'.encode(), bcrypt.gensalt()), 'name': 'Ram',
                'account_balance': 5000},
        'Lakshman': {'password': bcrypt.hashpw('Lakshman$123'.encode(), bcrypt.gensalt()), 'name': 'Lakshman',
                     'account_balance': 5500}
    }

    def login(username, password):
        if username in bank_users:
            stored_password = bank_users[username]['password']
            if bcrypt.checkpw(password.encode(), stored_password):
                print(
                    f"Welcome, {bank_users[username]['name']}! Your account balance is Rupees {bank_users[username]['account_balance']}.")
            else:
                print("Invalid password.")
        else:
            print("Username not found.")


    user_input_username = input("Enter your username: ")
    user_input_password = input("Enter your password: ")
    login(user_input_username, user_input_password)


def guess():
    global guess
    randomno = random.randint(1, 100)
    maxatt = 5

    print("WELCOME TO NUMBER GUESSING GAME")
    print(f"Guess the number between 1 and 100. You have {maxatt} attempts")

    for attempt in range(1, maxatt + 1):
        guess = int(input(f'Attempt {attempt}: Enter your guess: '))

        if guess == randomno:
            print("Congratulations! You've guessed the correct number!")
            break
        elif guess > randomno:
            print("Your guess is too high.")
        else:
            print("Your guess is too low.")

    if guess != randomno:
        print(f"You ran out of attempts! The correct number was {randomno}")
    print("Thank you for playing!")

import string

def strength():
    def passwordstrenght(password):
        lengthc = 8
        has_upper = False
        has_lower = False
        has_digit = False
        has_special = False

        special_characters = string.punctuation

        for char in password:
            if char.isupper():
                has_upper = True
            if char.islower():
                has_lower = True
            if char.isdigit():
                has_digit = True
            if char in special_characters:
                has_special = True

        strength = 0

        if len(password) >= lengthc:
            strength += 1
            if has_upper:
                strength += 1
            if has_lower:
                strength += 1
            if has_digit:
                strength += 1
            if has_special:
                strength += 1

        return strength

    # Example usage
    password = input("Enter your password: ")
    strength_value = passwordstrenght(password)

    # Determine the feedback
    if strength_value == 5:
        feedback = "Very Strong"
    elif strength_value == 4:
        feedback = "Strong"
    elif strength_value == 3:
        feedback = "Moderate"
    elif strength_value == 2:
        feedback = "Weak"
    else:
        feedback = "Very Weak"

    print(f"Your password strength is: {feedback}")


def store():

    def display_products(products):
        print("\nAvailable Products:")
        for product in products:
            print(f"Name: {product['name']}, Price: {product['price']}, Quantity: {product['quantity']}")


    def add_product(products):
        name = input("Enter the product name: ").strip()
        price = float(input("Enter the product price: "))
        quantity = int(input("Enter the quantity: "))

        for product in products:
            if product['name'].lower() == name.lower():
                print("Product already exists. Use update option to change the quantity.")
                return

        new_product = {'name': name, 'price': price, 'quantity': quantity}
        products.append(new_product)
        print(f"{name} added successfully!")


    def update_quantity(products):
        name = input("Enter the product name to update: ").strip()

        for product in products:
            if product['name'].lower() == name.lower():
                new_quantity = int(input("Enter the new quantity: "))
                product['quantity'] = new_quantity
                print(f"Quantity of {name} updated to {new_quantity}.")
                return

        print("Product not found.")


    def delete_product(products):
        name = input("Enter the product name to delete: ").strip()

        for product in products:
            if product['name'].lower() == name.lower():
                products.remove(product)
                print(f"{name} removed successfully!")
                return

        print("Product not found.")


    def main():
        products = []

        while True:
            print("\nGrocery Store Inventory Management")
            print("1. View Products")
            print("2. Add Product")
            print("3. Update Quantity")
            print("4. Delete Product")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                display_products(products)
            elif choice == "2":
                add_product(products)
            elif choice == "3":
                update_quantity(products)
            elif choice == "4":
                delete_product(products)
            elif choice == "5":
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")


    if __name__ == "__main__":
        main()



def day(name):
    match name:
        case 1:
            student_database()
        case 2:
            bank_database()
        case 3:
            pucsim()
        case 4:
            calculator()
        case 5:
            guess()
        case 6:
            strength()
        case 7:
            store()
        case _:
            return "Invalid Choice"


name = int(input("Enter your choice (1-7): \n"
                 "1. STUDENT DATABASE\n"
                 "2. BANK DATABASE\n"
                 "3. PUC SIMULATOR\n"
                 "4. CALCULATOR\n"
                 "5. NUMBER GUESSING GAME\n"
                 "6. PASSWORD STRENGTH FINDER\n"
                 "7. GROCERY STORE\n"))

result = day(name)
if result is not None:
    print(result)
