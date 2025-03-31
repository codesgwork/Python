def is_prime(n):
  if n < 2:
    return False
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False
  return True
def check_number(n):
  digit_sum = sum(int(digit) for digit in str(abs(n)))
  return not is_prime(digit_sum)
n = 1234
print(check_number(n))
