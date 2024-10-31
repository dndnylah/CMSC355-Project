import re
import datetime
import database
import base

current_year = datetime.datetime.now().year # initializes a variable later used for current year

# A function that tests if the user's first name is valid
def is_valid_first_name(first_name):
    pattern = r"^[a-zA-Z'-]" # The proper format of the input value
    return re.match(pattern,first_name) is not None # Compares input to pattern and returns a boolean value

# A function that tests if the user's last name is valid
def is_valid_last_name(last_name):
    pattern = r"^[a-zA-Z'-]" # The proper format of the input value
    return re.match(pattern,last_name) is not None # Compares input to pattern and returns a boolean value

# A function that tests if the user's email is valid
def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$" # The proper format of the input value
    return re.match(pattern, email) is not None # Compares input to pattern and returns a boolean value

# A function that tests if the user's phone number is valid
def is_valid_number(phone_number):
    pattern = r"^[0-9]" # The proper format of the input value
    if len(phone_number) != 10: # checks the length of the phone number, making sure its 10 digits long
        return False
    return re.match(pattern,phone_number) is not None # Compares input to pattern and returns a boolean value

# A function that tests if the user's birth year is valid
def is_valid_birth_year(birth_year):
    if len(birth_year) < 1: # Checks if the entry is null
        return 0
    birth_year = int(birth_year) # changes the string to an integer value
    low = 1910
    high = current_year
    if birth_year > low: # tests if birth year is greater than the lowest accepted value
            if birth_year <= high:
                return 1 # if the year is within or before the current year, the year is accepted
            else:
                return 0 # if the year isn't within the range, it is rejected
    else:
       return 0

# A function that tests if the user's password is valid
def is_secure_password(password):
    if len(password) < 8: # checks that the length is at least 8 characters
            print("Your password must be at least 8 characters long.\n")
            return False
    if not re.search("[A-Z]", password): # checks if the password has at least one capital letter
            print("Your password must contain at least one capital letter.\n")
            return False
    if not re.search("[a-z]", password): # checks if the password has at least one lowercase letter
            print("Your password must contain at least one lowercase letter.\n")
            return False
    if not re.search("[0-9]", password): # checks if the password contains at least one number
            print("Your password must contain at least one number.\n")
            return False
    if not re.search("[!@#$%^&*()_/-=+{}:;'\"|,.<>/?]", password): # checks the password for at least one special character
            print("Your password must contain at least one special character.\n")
            return False
    return True

# A function that tests if the user's repeated password matches the initial password
def is_repeated_password(repeatpassword, passwrd):
    if repeatpassword != passwrd: # tests if the passwords match
            print("The repeated password does not match the original.\n")
            return False
    return True

# A function that creates the user's profile given their signup information
def new_user_recursive():
    first_name = input("Please enter your first name.\n") # prompts user to input their first name
    if not is_valid_first_name(first_name): # tests if the user's input is valid
        print(f"{first_name} is not a valid first name.\n") # alerts user that their input is invalid
        while not is_valid_first_name(first_name): # allows the user to alter their input and tests the input until it is valid
            first_name = input("Please enter a valid first name.\n")
    database.add_first_name(first_name) # adds newly input user data into the database

    last_name = input("Please enter your last name.\n") # prompts user to input their last name
    if not is_valid_last_name(last_name): # tests if the user's input is valid
        print(f"{last_name} is not a valid last name.")
        while not is_valid_last_name(last_name): # allows the user to alter their input and tests the input until it is valid
            last_name = input("Please enter a valid last name.\n")
    database.add_last_name(last_name) # adds newly input user data into the database

    email = input("Please enter a valid email address.\n") # prompts user to input their email
    email = database.email_check(email) # checks database for duplicate emails
    if not is_valid_email(email): # tests if the user's input is valid
        print(f"{email} is not a valid email address.\n")
        while not is_valid_email(email): # allows the user to alter their input and tests the input until it is valid
            email = input("Please enter a valid email.\n")
    database.add_email(email) # adds newly input user data into the database

    phone_number = input("Please enter a valid phone number.\n") # prompts user to input their phone number
    if not is_valid_number(phone_number): # tests if the user's input is valid
        print(f"{phone_number} is not a valid phone number.\n")
        while not is_valid_number(phone_number): # allows the user to alter their input and tests the input until it is valid
            phone_number = input("Please enter a valid phone number.\n")
    database.add_number(phone_number) # adds newly input user data into the database

    birth_year = input("Please enter your birth year.\n") # prompts user to input their birth year
    if is_valid_birth_year(birth_year) == 0: # tests if the user's input is valid
            print(f"{birth_year} is not a valid birth year.\n")
            while is_valid_birth_year(birth_year) == 0: # allows the user to alter their input and tests the input until it is valid
                birth_year = input("Please enter a valid birth year.\n")
    database.add_birth_year(birth_year) # adds newly input user data into the database

    password = input("Enter a password.\n") # prompts user to input their password
    if not is_secure_password(password): # tests if the user's input is valid
            while not is_secure_password(password): # allows the user to alter their input and tests the input until it is valid
                password = input("Please enter a secure password.\n")
    database.add_password(password) # adds newly input user data into the database

    repeatPassword = input("Re-enter password.\n") # prompts user to reenter their password
    if not is_repeated_password(repeatPassword, password): # tests if the user's input is valid
            while not is_repeated_password(repeatPassword, password): # allows the user to alter their input and tests the input until it is valid
                repeatPassword = input("Passwords must match, please try again.\n")

    terms = input("Do you agree to our terms and conditions?\n") # prompts user to agree to terms
    terms = terms.lower() # makes entire string lower case
    if terms.__contains__('y'): # if the user inputs 'yes' the account is created
        print("Your account has been created, please login.\n")
        base.welcome() # returns user to home login/signup screen
    else:
        print("We are unable to create your account.\n") # if the user doesn't enter yes, the account is voided
        base.welcome() # returns user to home page











