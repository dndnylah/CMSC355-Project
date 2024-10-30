import database
import signup

def welcome():
    choice = input("Hello! Would you like to sign up or login?\n")
    if choice.lower().__contains__('sign'):
        signup.new_user_recursive()
