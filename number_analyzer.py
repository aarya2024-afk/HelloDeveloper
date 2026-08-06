num = int(input("Enter a number: "))

# Even or Odd
if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# Positive, Negative or Zero
if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")

# Prime or Not Prime
if num <= 1:
    print("Not a Prime Number")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime Number")
    else:
        print("Not a Prime Number")

# Palindrome or Not
original = str(num)

if original == original[::-1]:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")