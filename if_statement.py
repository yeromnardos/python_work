num = int(input("Enter number:"))

if num % 2 == 0:
    print(f"{num} is even number")
else:
    print(f"{num} is odd number")

age = int(input("Enter age:"))
if age >= 18 and age <= 100:
    print(f"{age} is able to vote")
else:
    print(f"{age} is not able to vote")
