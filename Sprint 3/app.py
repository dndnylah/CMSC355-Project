import tkinter as tkinter
from tkinter import messagebox


# Function to center a window on the screen
def center_window(win, width, height):
    """Center the given window on the screen."""
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    win.geometry(f"{width}x{height}+{x}+{y}")


# Initialize the main window
window = tkinter.Tk()
window.title("User Authentication")
window.geometry('400x500')
center_window(window, 400, 500)  # Center the window
window.configure(bg='#011111')  # Dark green background


# Placeholder for user credentials (credentials will be stored in database)
credentials = {"user1@example.com": "password123"}


def validate_email(email):
    """Check if email is valid."""
    return "@" in email and email.endswith(".com")


def login():
    """Handle the login process."""
    email = email_entry.get()
    password = password_entry.get()

    # Check for empty fields
    if not email and not password:
        messagebox.showerror("Login Failed", "Please fill in the email and password.")
        return
    elif not email:
        messagebox.showerror("Login Failed", "Please fill in the email.")
        return
    elif not password:
        messagebox.showerror("Login Failed", "Please fill in the password.")
        return

    # Validate email format
    if not validate_email(email):
        messagebox.showerror("Login Failed", "Make sure input is a valid email.")
        return

    # Validate credentials
    if email in credentials and credentials[email] == password:
        messagebox.showinfo("Login Successful", "Successfully logged in!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")


def forgot_password_screen():
    """Show the Forgot Password screen."""
    forgot_window = tkinter.Toplevel(window)
    forgot_window.title("Forgot Password")
    forgot_window.geometry('400x300')  # Set size
    center_window(forgot_window, 400, 300)  # Center the window
    forgot_window.configure(bg='#011111')  # Dark green background

    tkinter.Label(forgot_window, text="Forgot Password", font=("Arial", 24), bg='#011111', fg='#FFF').pack(pady=20)  
    tkinter.Label(forgot_window, text="Please enter email of account", font=("Arial", 16), bg='#011111', fg='#FFF').pack(pady=10)

    forgot_email_entry = tkinter.Entry(forgot_window, font=("Arial", 16))
    forgot_email_entry.pack(pady=10)

    def handle_forgot_password():
        """Handle the forgot password validation."""
        email = forgot_email_entry.get()
        if not email:
            messagebox.showerror("Error", "Please enter an email.")
            return

        if validate_email(email):
            messagebox.showinfo("Password Recovery", "Email has been sent to account if account exists.")
            forgot_window.destroy()
        else:
            messagebox.showerror("Error", "Please enter a valid email.")

    tkinter.Button(forgot_window, text="Submit", bg='#033', fg='#FFF', font=("Arial", 14), command=handle_forgot_password).pack(pady=20)  


def show_signup_screen():
    """Show the sign-up screen."""
    signup_window = tkinter.Toplevel(window)
    signup_window.title("Sign Up")
    signup_window.geometry('400x500')
    center_window(signup_window, 400, 500)  # Center the window
    signup_window.configure(bg='#011111')  

    tkinter.Label(signup_window, text="Sign Up", font=("Arial", 24), bg='#011111', fg='#FFF').pack(pady=20)  

    tkinter.Label(signup_window, text="Email", font=("Arial", 16), bg='#011111', fg='#FFF').pack(pady=5)
    signup_email_entry = tkinter.Entry(signup_window, font=("Arial", 16))
    signup_email_entry.pack(pady=5)

    tkinter.Label(signup_window, text="Password", font=("Arial", 16), bg='#011111', fg='#FFF').pack(pady=5)
    signup_password_entry = tkinter.Entry(signup_window, show="*", font=("Arial", 16))
    signup_password_entry.pack(pady=5)

    tkinter.Label(signup_window, text="Confirm Password", font=("Arial", 16), bg='#011111', fg='#FFF').pack(pady=5)
    signup_confirm_password_entry = tkinter.Entry(signup_window, show="*", font=("Arial", 16))
    signup_confirm_password_entry.pack(pady=5)

    def handle_signup():
        """Handle the sign-up process."""
        email = signup_email_entry.get()
        password = signup_password_entry.get()
        confirm_password = signup_confirm_password_entry.get()

        if not email or not password or not confirm_password:
            messagebox.showerror("Sign Up Failed", "All fields are required.")
            return

        if not validate_email(email):
            messagebox.showerror("Sign Up Failed", "Make sure input is a valid email.")
            return

        if password != confirm_password:
            messagebox.showerror("Sign Up Failed", "Passwords do not match.")
            return

        if email in credentials:
            messagebox.showerror("Sign Up Failed", "An account with this email already exists.")
            return

        credentials[email] = password
        messagebox.showinfo("Sign Up Successful", "Your account has been created!")
        signup_window.destroy()

    tkinter.Button(signup_window, text="Sign Up", bg='#033', fg='#FFF', font=("Arial", 14), command=handle_signup).pack(pady=20)  # Teal button


def show_login_screen():
    """Show the login screen."""
    clear_window()

    login_frame = tkinter.Frame(bg='#011111')  
    login_frame.pack(fill='both', expand=True)

    tkinter.Label(login_frame, text="Log In", font=("Arial", 24), bg='#011111', fg='#FFF').pack(pady=20)  

    global email_entry, password_entry
    tkinter.Label(login_frame, text="Email", font=("Arial", 16), bg='#011111', fg='#FFF').pack(pady=5)
    email_entry = tkinter.Entry(login_frame, font=("Arial", 16))
    email_entry.pack(pady=5)

    tkinter.Label(login_frame, text="Password", font=("Arial", 16), bg='#011111', fg='#FFF').pack(pady=5)
    password_entry = tkinter.Entry(login_frame, show="*", font=("Arial", 16))
    password_entry.pack(pady=5)

    tkinter.Button(login_frame, text="Login", bg='#033', fg='#FFF', font=("Arial", 14), command=login).pack(pady=10)  
    tkinter.Button(login_frame, text="Forgot Password?", bg='#033', fg='#FFF', font=("Arial", 12), command=forgot_password_screen).pack(pady=5)  


def show_home_screen():
    """Show the home screen with Sign Up and Log In options."""
    clear_window()

    home_frame = tkinter.Frame(bg='#011111')  
    home_frame.pack(fill='both', expand=True)

    tkinter.Label(home_frame, text="Welcome!", font=("Arial", 24), bg='#011111', fg='#FFF').pack(pady=50)  
    tkinter.Button(home_frame, text="Sign Up", bg='#033', fg='#FFF', font=("Arial", 16), command=show_signup_screen).pack(pady=20)  
    tkinter.Button(home_frame, text="Log In", bg='#033', fg='#FFF', font=("Arial", 16), command=show_login_screen).pack(pady=20)  


def clear_window():
    """Clear all widgets from the main window."""
    for widget in window.winfo_children():
        widget.destroy()


# Start the application
show_home_screen()
window.mainloop()
