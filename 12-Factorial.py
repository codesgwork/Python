def factorial(x):
  result = 1
  while x > 1:
    result *= x
    x -= 1
  return result
num = 5
factorial_num = factorial(num)
print(factorial_num)
