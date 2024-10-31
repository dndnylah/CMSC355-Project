
import signup

# A home page function that allows the user to sign up or login
def welcome():
    choice = input("Hello! Would you like to sign up or login?\n")
    if choice.lower().__contains__('sign'):
        signup.new_user_recursive() # calls to the signup.py file
    else:
        exit() # exits program

welcome() # A call to the function to begin program
