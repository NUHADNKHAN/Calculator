def add(num1, num2):
  """Adds two numbers."""
  return num1 + num2

def subtract(num1, num2):
  """Subtracts two numbers."""
  return num1 - num2

def multiply(num1, num2):
  """Multiplies two numbers."""
  return num1 * num2

def divide(num1, num2):
  """Divides two numbers."""
  return num1 / num2

def main():
  """The main function."""
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))

  operation = input("Choose an operation (+, -, *, /): ")

  if operation == "+":
    print(num1, "+", num2, "=", add(num1, num2))
  elif operation == "-":
    print(num1, "-", num2, "=", subtract(num1, num2))
  elif operation == "*":
    print(num1, "*", num2, "=", multiply(num1, num2))
  elif operation == "/":
    print(num1, "/", num2, "=", divide(num1, num2))
  else:
    print("Invalid operation.")

if __name__ == "__main__":
  main()
