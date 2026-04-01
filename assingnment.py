# Dictionary to store birthdays
birthdays = {}

# Take number of people
n = int(input("Enter number of people: "))

# Store data
for i in range(n):
    name = input("Enter name: ")
    day = int(input("Enter birthday day: "))
    month = int(input("Enter birthday month: "))
    
    birthdays[name] = (day, month)

# Take today's date
today_day = int(input("Enter today's day: "))
today_month = int(input("Enter today's month: "))

# Function to calculate days (simplified, ignoring leap years)
def days_from_start(day, month):
    days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    total = sum(days_in_month[:month-1]) + day
    return total

today_total = days_from_start(today_day, today_month)

# Check birthdays today
found = False
print("\n--- Today's Birthdays ---")
for name, date in birthdays.items():
    if date[0] == today_day and date[1] == today_month:
        print("🎉 Today is", name, "'s birthday!")
        found = True

if not found:
    print("No birthdays today.")

# Show upcoming birthdays
print("\n--- Upcoming Birthdays ---")
for name, (day, month) in birthdays.items():
    bday_total = days_from_start(day, month)
    
    if bday_total >= today_total:
        days_left = bday_total - today_total
    else:
        days_left = 365 - today_total + bday_total
    
    print(name, "-> in", days_left, "days")

# Search for a person's birthday
search = input("\nEnter a name to search birthday: ")

if search in birthdays:
    day, month = birthdays[search]
    print(search, "'s birthday is on:", day, "/", month)
else:
    print("Person not found.")
