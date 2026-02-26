# Take user input
name = input("Enter name: ")
birthday_day = int(input("Enter birthday day: "))
birthday_month = int(input("Enter birthday month: "))

# Take today's date from user
today_day = int(input("Enter today's day: "))
today_month = int(input("Enter today's month: "))

# Check birthday
if birthday_day == today_day and birthday_month == today_month:
    print("Today is", name, "birthday!")
else:
    print("No birthday today.")