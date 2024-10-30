import re
import datetime
import database
import base

current_year = datetime.datetime.now().year

def is_valid_first_name(first_name):
    pattern = r"^[a-zA-Z'-]"
    return re.match(pattern,first_name) is not None

def is_valid_last_name(last_name):
    pattern = r"^[a-zA-Z'-]"
    return re.match(pattern,last_name) is not None

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None

def is_valid_number(phone_number):
    pattern = r"^\+?[0-9]\d{7,14}$"
    return re.match(pattern,phone_number) is not None

def is_valid_birth_year(birth_year):
    birth_year = int(birth_year)
    low = 1910
    high = current_year
    if birth_year > low:
            if birth_year <= high:
                return 1
            else:
                return 0
    else:
       return 0

def is_secure_password(password):
    if len(password) < 8:
            print("Your password must be at least 8 characters long.\n")
            return False
    if not re.search("[A-Z]", password):
            print("Your password must contain at least one capital letter.\n")
            return False
    if not re.search("[a-z]", password):
            print("Your password must contain at least one lowercase letter.\n")
            return False
    if not re.search("[0-9]", password):
            print("Your password must contain at least one number.\n")
            return False
    if not re.search("[!@#$%^&*()_/-=+{}:;'\"|,.<>/?]", password):
            print("Your password must contain at least one special character.\n")
            return False
    return True

def is_repeated_password(repeatpassword, passwrd):
    if repeatpassword != passwrd:
            print("The repeated password does not match the original.\n")
            return False
    return True

def new_user_recursive():
    first_name = input("Please enter your first name.\n")
    if not is_valid_first_name(first_name):
        print(f"{first_name} is not a valid first name.\n")
        while not is_valid_first_name(first_name):
            first_name = input("Please enter a valid first name.\n")
    database.add_first_name(first_name)

    last_name = input("Please enter your last name.\n")
    if not is_valid_last_name(last_name):
        print(f"{last_name} is not a valid last name.")
        while not is_valid_last_name(last_name):
            last_name = input("Please enter a valid last name.\n")
    database.add_last_name(last_name)

    email = input("Please enter a valid email address.\n")
    email = database.email_check(email)
    if not is_valid_email(email):
        print(f"{email} is not a valid email address.\n")
        while not is_valid_email(email):
            email = input("Please enter a valid email.\n")
    database.add_email(email)

    phone_number = input("Please enter a valid phone number.\n")
    if not is_valid_number(phone_number):
        print(f"{phone_number} is not a valid phone number.\n")
        while not is_valid_number(phone_number):
            email = input("Please enter a valid phone number.\n")
    database.add_number(phone_number)

    birth_year = input("Please enter your birth year.\n")
    if is_valid_birth_year(birth_year) == 0:
            print(f"{birth_year} is not a valid birth year.\n")
            while is_valid_birth_year(birth_year) == 0:
                birth_year = input("Please enter a valid birth year.\n")
    database.add_birth_year(birth_year)

    password = input("Enter a password.\n")
    if not is_secure_password(password):
            while not is_secure_password(password):
                password = input("Please enter a secure password.\n")
    database.add_password(password)

    repeatPassword = input("Re-enter password.\n")
    if not is_repeated_password(repeatPassword, password):
            while not is_repeated_password(repeatPassword, password):
                repeatPassword = input("Passwords must match, please try again.\n")

    terms = input("Do you agree to our terms and conditions?\n")
    terms = terms.lower()
    if terms.__contains__('y'):
        print("Your account has been created, please login.\n")
        base.welcome()
    else:
        print("We are unable to create your account.\n")











