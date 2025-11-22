#!/usr/bin/env python3
from datetime import datetime, timedelta

def display_current_datetime():
    # Save the current date inside current_date variable
    current_date = datetime.now()

    # Format the date and time: YYYY-MM-DD HH:MM:SS
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")

    print("Current date and time:", formatted)

    # Return it in case you need it
    return current_date


def calculate_future_date(current_date, days_to_add):
    # Save the future date inside future_date variable
    future_date = current_date + timedelta(days=days_to_add)

    # Format future date as YYYY-MM-DD
    formatted = future_date.strftime("%Y-%m-%d")

    print("Future date:", formatted)

    return future_date


def main():
    # Part 1 - Display current date/time
    current_date = display_current_datetime()

    # Part 2 - Ask user for days to add
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(current_date, days)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    main()

