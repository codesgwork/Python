def check_balance(balance):
  print("Your balance is $", balance)
def deposit(balance):
  amount = float(input("Enter amount to deposit: "))
  if amount <= 0:
    print("Amount must be greater than 0")
  else:
    balance += amount
  return balance
def withdraw(balance):
  amount = float(input("Enter amount to withdraw: "))
  if amount > balance:
    print("Insufficient balance")
  elif amount <= 0:
    print("Amount must be greater than 0")
  else:
    balance -= amount
  return balance
def loan(balance):
  amount = float(input("Enter amount to loan: "))
  if amount <= 0:
    print("Amount must be greater than 0")
  else:
    balance += amount
  return balance
def transfer(balance):
  amount = float(input("Enter amount to transfer: "))
  if amount > balance:
    print("Insufficient balance")
  elif amount <= 0:
    print("Amount must be greater than 0")
  else:
    balance -= amount
  return balance
