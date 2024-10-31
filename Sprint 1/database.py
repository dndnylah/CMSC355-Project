# initializes each list based on the input variable type
first_name_list = list()
last_name_list = list()
email_list = list()
number_list = list()
birth_year_list = list()
password_list = list()

# A function to check the database's existing emails and compare them to the new user's emails to prevent duplications
def email_check(email):
    if email_list.__contains__(email):
        print("An account with this email already exists.\n")
        email = " " # resets email string so it prompts user to enter a different email
    return email # returns the empty string

# A function that adds the user's first name to the first name list
def add_first_name(first_name):
    first_name_list.append(first_name)

# A function that adds the user's last name to the first name list
def add_last_name(last_name):
    last_name_list.append(last_name)

# A function that adds the user's email to the first name list
def add_email(email):
    email_list.append(email)

# A function that adds the user's phone number to the first name list
def add_number(number):
    number_list.append(number)

# A function that adds the user's birth year to the first name list
def add_birth_year(year):
    birth_year_list.append(year)

# A function that adds the user's password to the first name list
def add_password(password):
    password_list.append(password)





