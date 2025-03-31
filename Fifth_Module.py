import random
def spin_row(Symbols):
  spin = [random.choice(Symbols) for i in range(3)]
  return spin
def print_row(Symbols):
  return " ".join(spin_row(Symbols))
