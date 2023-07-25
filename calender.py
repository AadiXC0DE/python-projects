from calendar import monthrange
from datetime import datetime

# Function to display the calendar
def display_calendar(year, month, events):
    now = datetime.now()
    current_year, current_month = now.year, now.month

    if year == current_year and month == current_month:
        print(now.strftime(" %B %Y ").center(20, "-"))
    else:
        print(datetime(year, month, 1).strftime(" %B %Y ").center(20, "-"))

    print("Mo Tu We Th Fr Sa Su")

    _, num_days = monthrange(year, month)
    first_day = datetime(year, month, 1).weekday()

    day_counter = 1

    for _ in range((first_day + 1) % 7):
        print("   ", end=" ")

    for day in range(1, num_days + 1):
        if events.get((year, month, day)):
            event = events[(year, month, day)]
            print(f"{day:2}*", end=" ")
        else:
            print(f"{day:2} ", end=" ")
        day_counter += 1
        if day_counter % 7 == 1:
            print()

    print("\n")

# Function to add an event to the calendar
def add_event(events, year, month, day, event):
    events[(year, month, day)] = event
    print("Event added successfully!")

# Function to view events for a specific day
def view_events(events, year, month, day):
    event = events.get((year, month, day))
    if event:
        print(f"Events for {year}-{month:02}-{day:02}:")
        print(f"- {event}")
    else:
        print("No events for this day.")

# Main function to run the calendar
def main():
    events = {}

    while True:
        now = datetime.now()
        year = now.year
        month = now.month

        display_calendar(year, month, events)

        print("Menu:")
        print("1. Add event")
        print("2. View events")
        print("3. Quit")

        choice = input("Select an option (1/2/3): ")

        if choice == "1":
            day = int(input("Enter the day: "))
            event = input("Enter the event: ")
            add_event(events, year, month, day, event)
        elif choice == "2":
            day = int(input("Enter the day: "))
            view_events(events, year, month, day)
        elif choice == "3":
            print("Exiting calendar...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
