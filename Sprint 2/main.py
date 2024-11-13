import database
from datetime import datetime
from checkin import CheckIn # fix error when you 

def main():
    checkin = CheckIn()

    # Display the missed check-ins count from the last entry
    if database.missed_checkins_list:
        missed_checkins = database.missed_checkins_list[-1]  # Get the last entry's missed check-in count
        print(f"Welcome! It has been {missed_checkins} day(s) since your last check-in.")
    else:
        print("Welcome! This is your first check-in.")

    # Ask the user if they want to check-in manually
    action = input("Would you like to check-in manually? (yes/no): ").strip().lower()
    
    if action == "yes":
        checkin.manual_checkin()
    else:
        # Log a missed check-in if the user skips the manual check-in
        missed_checkins = database.missed_checkins_list[-1] + 1 if database.missed_checkins_list else 1
        database.add_date(datetime.now().strftime("%Y-%m-%d"))
        database.add_medication_taken(False)
        database.add_rating(None)
        database.add_comments(None)
        database.add_missed_checkins(missed_checkins)
        print("Returning to home screen without checking in.")

if __name__ == "__main__":
    main()