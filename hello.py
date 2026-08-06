from datetime import datetime

# Student Details
name = "Aarya Agarwal"
register_number = "24MIS0145"
department = "Computer Science"

# Current Date and Time
now = datetime.now()

print("=" * 40)
print("         HELLO DEVELOPER")
print("=" * 40)
print(f"Name            : {name}")
print(f"Register Number : {register_number}")
print(f"Department      : {department}")
print(f"Current Date    : {now.strftime('%d-%m-%Y')}")
print(f"Current Time    : {now.strftime('%I:%M:%S %p')}")
print("=" * 40)