# Initializing lists for each data field in the medication check-in records
date_list = list()
medication_taken_list = list()
rating_list = list()
comments_list = list()
missed_checkins_list = list()

# Function to check if a check-in already exists for a given date (prevents duplicate entries for the same day)
def date_check(date):
    if date in date_list:
        print("A check-in for this date already exists.\n")
        date = ""  # Resets date to prompt the user for a different entry
    return date

# Functions to add entries to each respective list

def add_date(date):
    date_list.append(date)

def add_medication_taken(medication_taken):
    medication_taken_list.append(medication_taken)

def add_rating(rating):
    rating_list.append(rating)

def add_comments(comments):
    comments_list.append(comments)

def add_missed_checkins(missed_checkins):
    missed_checkins_list.append(missed_checkins)

# Sample function to simulate a check-in process

def log_checkin(date, medication_taken, rating=None, comments=None, missed_checkins=0):
    # Check if a check-in for this date already exists
    date = date_check(date)
    if not date:  # if date is an empty string after date_check, return early
        return

    # Add entries to respective lists
    add_date(date)
    add_medication_taken(medication_taken)
    add_rating(rating)
    add_comments(comments)
    add_missed_checkins(missed_checkins)
    print("Check-in logged successfully.\n")
