# daily_reminder.py

task = input("Enter your task: ")

# Loop to ensure priority is valid
while True:
    priority = input("Priority (high/medium/low): ").lower()
    if priority in ["high", "medium", "low"]:
        break
    print("Invalid priority. Please enter high, medium, or low.")

time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process task priority
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority level"

# Modify message if time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder = "Note: " + reminder + ". Consider completing it when you have free time."

# Output the final reminder
print("\nReminder:", reminder)
