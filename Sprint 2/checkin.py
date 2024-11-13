from datetime import datetime

# Import lists from database
import database

class CheckIn:
    def confirm_medication(self):
        response = input("Have you taken your medication today? (yes/no): ").strip().lower()
        return response == "yes"

    def get_rating(self):
        while True:
            try:
                rating = int(input("Rate how you're feeling on a scale of 1-5: "))
                if 1 <= rating <= 5:
                    return rating
                else:
                    print("Please enter a rating between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 5.")

    def get_comments(self):
        return input("Enter additional comments about your rating: ")

    def manual_checkin(self):
        # Confirm medication
        if self.confirm_medication():
            # Prompt for a check-in
            checkin_choice = input("Would you like to check in with a rating today? (yes/no): ").strip().lower()
            if checkin_choice == "yes":
                # Get today's date
                date_today = datetime.now().strftime("%Y-%m-%d")
                
                # Check for duplicate date entry
                date_today = database.date_check(date_today)
                if not date_today:  # Date exists; end early if duplicate
                    return
                
                # Collect rating and comments
                rating = self.get_rating()
                comments = self.get_comments()

                # Log check-in details to lists
                database.add_date(date_today)
                database.add_medication_taken(True)
                database.add_rating(rating)
                database.add_comments(comments)
                database.add_missed_checkins(0)  # Reset missed check-ins to 0
                print("Check-in submitted successfully.")
            else:
                # Increment missed check-ins if the user selects "no" for check-in
                missed_checkins = database.missed_checkins_list[-1] + 1 if database.missed_checkins_list else 1
                database.add_date(datetime.now().strftime("%Y-%m-%d"))
                database.add_medication_taken(False)
                database.add_rating(None)
                database.add_comments(None)
                database.add_missed_checkins(missed_checkins)
                print("Check-in skipped. Returning to the home screen.")
        else:
            print("Check-in not submitted. Please confirm you have taken your medication.")
