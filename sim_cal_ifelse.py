num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
operation = input("Enter operation(+,-,*,/):")
if operation == '+':
  print("Result:" , num1 + num2)
elif operation == '-':
  print("Result:" , num1 - num2)
elif operation == '*':
  print("Result:" , num1 * num2)
elif operation == n'/':
  print("Result:" , num1 / num2)
elif operation == '%':
  print("Result:" , num1 % num2)
elif operation == '//':
  print("result:" , num1 // num2)  
else:
  print("Invalid operation")
