import datetime

subscriptions = {}

while True:
    sub_name = input("Enter subscription name (or type 'quit' to exit): ")
    if sub_name == 'quit':
        break
    start_date_str = input("Enter start date (YYYY-MM-DD): ")
    end_date_str = input("Enter end date (YYYY-MM-DD): ")
    start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d').date()
    end_date = datetime.datetime.strptime(end_date_str, '%Y-%m-%d').date()
    days_left = (end_date - datetime.date.today()).days
    subscriptions[sub_name] = days_left
    print(f"{sub_name} expires in {days_left} days.")

print("Current subscriptions:")
for sub_name, days_left in subscriptions.items():
    print(f"{sub_name} expires in {days_left} days.")