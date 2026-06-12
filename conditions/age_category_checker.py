n = int(input("Enter your age: "))

if n < 13:
    print("This is child")
elif n >= 13 and n <= 19:
    print("This is teen")
elif n >= 20 and n <= 59:
    print("This is adult")
else:
    print("This is senior citizen")
