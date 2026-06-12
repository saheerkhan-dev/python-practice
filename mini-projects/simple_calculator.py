a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("result:", a + b)
elif choice == 2:
    print("result:", a - b)
elif choice == 3:
    print("result:", a * b)
elif choice == 4:
    print("result:", a / b)
else:
    print("Invalid choice")
