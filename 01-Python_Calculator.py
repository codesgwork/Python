is_running = True
while is_running:
    operator = input("Please select any operator (+, -, *, /): ")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    if operator == "+":
        print("The sum of the two numbers is: ", num1 + num2)
        is_running = False
    elif operator == "-":
        print("The difference of the two numbers is: ", num1 - num2)
        is_running = False
    elif operator == "*":
        print("The product of the two numbers is: ", num1 * num2)
        is_running = False
    elif operator == "/":
        print("The division of the two numbers is: ", num1 / num2)
        is_running = False
    else:
        print("Please select a valid operator")
        continue
