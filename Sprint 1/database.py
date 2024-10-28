import signup

first_name_list = list()
last_name_list = list()
email_list = list()
birth_year_list = list()
password_list = list()

def email_check(email):
    if email_list.__contains__(signup.email):
        print("An account with this email already exists.\n")
        signup.email = " "
def add_data():
    first_name_list.append(signup.first_name)
    last_name_list.append(signup.last_name)
    email_list.append(signup.email)
    birth_year_list.append(signup.birth_year)
    password_list.append(signup.password)

    print(first_name_list, last_name_list, email_list, birth_year_list, password_list)

