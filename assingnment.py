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

# Check birthdays
found = False

for name, date in birthdays.items():
    if date[0] == today_day and date[1] == today_month:
        print("Today is", name, "birthday!")
        found = True

if not found:
    print("No birthdays today.")