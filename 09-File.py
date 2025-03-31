# Exclusive
file_path = "Ninth_File.txt"
file_txt = "I like pizza!"
try:
  with open(file_path, "x") as file:
    file.write(file_txt)
    print("Txt file '" + file_path + "' has been created.")
except FileExistsError:
  print("The file already exits!")
# Write
file_path = "Ninth_File2.txt"
file_txt = "I like pizza!"
with open(file_path, "w") as file:
  file.write(file_txt)
  print("Txt file '" + file_path + "' has been created.")
