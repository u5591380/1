from datetime import datetime

def date_passed(todays_date, scheduled_date):
    # Convert date strings to datetime objects
    today = datetime.strptime(todays_date, '%dth %B')
    scheduled = datetime.strptime(scheduled_date, '%dth %B')

    # Compare dates and print the appropriate message
    if today < scheduled:
        print("Scheduled date is yet to pass.")
    elif today > scheduled:
        print("Scheduled date has passed.")
    else:
        print("Scheduled date is today.")

# Test cases
date_passed("26th March", "25th March")  # Expected: Scheduled date has passed
date_passed("26th March", "26th March")  # Expected: Scheduled date is today
date_passed("26th March", "27th March")  # Expected: Scheduled date is yet to pass
