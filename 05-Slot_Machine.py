import time
import random
import Fifth_Module as fm
print("Welcome to the Slot Machine Program!")
time.sleep(1)
amount = 100
time.sleep(1)
print("(^_^)")
time.sleep(1)
while amount > 0:
  print("********************************")
  print("You have $", amount, "left.")
  print("Symbols: 🍒 | 🎰 | 🔔 | 💎 | 🐍")
  print("********************************")
  time.sleep(1)
  Symbols = ["🍒", "🎰", "🔔", "💎", "🐍"]
  time.sleep(1)
  play_game = input("Do you want to play? (y/n)")
  time.sleep(1)
  if play_game.lower() == "y":
    print("Spinning...")
    time.sleep(1)
    fm.spin_row(Symbols)
    time.sleep(1)
    row = fm.print_row(Symbols)
    time.sleep(1)
    print(row)
    if row[0] == row[1] == row[2]:
      if row[0] == "🍒":
        amount += 10
        print("You won $10!")
      elif row[0] == "🎰":
        amount += 20
        print("You won $20!")
      elif row[0] == "🔔":
        amount += 30
        print("You won $30!")
      elif row[0] == "💎":
        amount += 40
        print("You won $40!")
      else:
        amount += 50
        print("You won $50!")
  else:
    print("********************************")
    print("Thank you for playing!")
    print("********************************")
    break
time.sleep(1)
print("********************************")
print("Game Over!")
print("********************************")
time.sleep(1)
print("********************************")
print("You have $", amount, "left.")
print("********************************")
