import time
import random
import string
print("Welcome to the Encryption Program")
time.sleep(1)
chars = string.ascii_letters + string.digits + string.punctuation + " "
chars = list(chars)
key = chars.copy()
random.shuffle(key)
plain_text = input("Enter the text you want to encrypt: ")
cipher_text = ""
for i in plain_text:
  cipher_text += key[chars.index(i)]
print("The encrypted text is: ", cipher_text)
cipher_text = input("Enter the text you want to decrypt: ")
plain_text = ""
for i in cipher_text:
  plain_text += chars[key.index(i)]
