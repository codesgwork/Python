from Fourth_Package import Banking_Functions
import time
print("Welcome to the Banking App Program!")
time.sleep(1)
is_running = True
time.sleep(1)
print("(^_^)")
time.sleep(1)
while is_running:
  username = input("Enter your username: ")
  password = input("Enter your password: ")
  if username == "admin" and password == "admin":
    print("Welcome, admin!")
    time.sleep(1)
    break
  else:
    print("Invalid username or password!")
    is_running = False
balance = 0
while is_running:
  time.sleep(1)
  print("********************************")
  print("        Bank Acount        ")
  print("********************************")
  time.sleep(1)
  print("1. Check Balance")
  time.sleep(1)
  print("2. Deposit")
  time.sleep(1)
  print("3. Withdraw")
  time.sleep(1)
  print("4. Loan")
  time.sleep(1)
  print("5. Transfer")
  time.sleep(1)
  print("6. Exit")
  time.sleep(1)
  print("********************************")
  option = int(input("Enter your option (1, 2, 3, 4, 5 and 6): "))
  if option == 1:
    Banking_Functions.check_balance(balance)
  elif option == 2:
    balance = Banking_Functions.deposit(balance)
  elif option == 3:
    balance = Banking_Functions.withdraw(balance)
  elif option == 4:
    balance = Banking_Functions.loan(balance)
  elif option == 5:
    balance = Banking_Functions.transfer(balance)
  elif option == 6:
    print("Thank you for using the Banking App Program!")
    is_running = False
  else:
    print("Invalid option!")
