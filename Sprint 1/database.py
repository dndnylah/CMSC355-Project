import signup

first_name_list = list()
last_name_list = list()
email_list = list()
number_list = list()
birth_year_list = list()
password_list = list()

def email_check(email):
    if email_list.__contains__(email):
        print("An account with this email already exists.\n")
        email = " "
    return email
def add_first_name(first_name):
    first_name_list.append(first_name)

def add_last_name(last_name):
    last_name_list.append(last_name)

def add_email(email):
    email_list.append(email)

def add_number(number):
    number_list.append(number)

def add_birth_year(year):
    birth_year_list.append(year)

def add_password(password):
    password_list.append(password)





