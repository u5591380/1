def speeding_ticket(speed, is_birthday):
    # Adjust speed limits on birthday
    if is_birthday:
        speed -= 5

    # Check speed and determine ticket category
    if speed <= 60:
        return "No Ticket"
    elif 61 <= speed <= 80:
        return "Small Ticket"
    else:
        return "Big Ticket"

# Example usage:
speed = 70
birthday = False  # Change to True if it's the driver's birthday
result = speeding_ticket(speed, birthday)
print(result)
