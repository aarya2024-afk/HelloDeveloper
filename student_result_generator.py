print("========== STUDENT RESULT GENERATOR ==========")

name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")

marks = []

for i in range(1, 6):
    mark = float(input(f"Enter marks for Subject {i}: "))
    marks.append(mark)

total = sum(marks)
average = total / 5
percentage = average

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n========== RESULT ==========")
print(f"Student Name : {name}")
print(f"Roll Number  : {roll}")
print(f"Total Marks  : {total}/500")
print(f"Average      : {average:.2f}")
print(f"Percentage   : {percentage:.2f}%")
print(f"Grade        : {grade}")

if grade == "F":
    print("Result       : FAIL")
else:
    print("Result       : PASS")
    