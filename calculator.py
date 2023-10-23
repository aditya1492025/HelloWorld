def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

def main():
  print("**Menu-Driven Calculator**")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")

  choice = int(input("Enter your choice: "))

  if choice == 1:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    result = add(a, b)
    print(f"{a} + {b} = {result}")
  elif choice == 2:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    result = subtract(a, b)
    print(f"{a} - {b} = {result}")
  elif choice == 3:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    result = multiply(a, b)
    print(f"{a} * {b} = {result}")
  elif choice == 4:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    result = divide(a, b)
    print(f"{a} / {b} = {result}")
  else:
    print("Invalid choice.")

if __name__ == "__main__":
  main()
