from Third_Package import Math_Module
operator = input("Enter the operator (+, -, * and /): ")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if operator == '+':
  print(Math_Module.add(num1, num2))
elif operator == '-':
  print(Math_Module.subtract(num1, num2))
elif operator == '*':
  print(Math_Module.multiply(num1, num2))
elif operator == '/':
  print(Math_Module.divide(num1, num2))
elif operator == '%':
  print(Math_Module.remainder(num1, num2))
elif operator == '//':
  print(Math_Module.integer_divide(num1, num2))
elif operator == '**':
  print(Math_Module.power(num1, num2))
elif operator == 'square':
  print(Math_Module.square(num1))
elif operator == 'square_root':
  print(Math_Module.square_root(num1))
elif operator == 'cube':
  print(Math_Module.cube(num1))
elif operator == 'cube_root':
  print(Math_Module.cube_root(num1))
elif operator == 'absolute':
  print(Math_Module.absolute(num1))
else:
  print("Invalid Operator")
