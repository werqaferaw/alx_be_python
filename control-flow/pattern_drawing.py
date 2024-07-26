while True:
  try:
    size = int(input("Enter the size of the pattern (positive integer): "))
    if size > 0:
      break
    else:
      print("Please enter a positive integer.")
  except ValueError:
    print("Invalid input. Please enter a number.")


for i in range(size):
  for j in range(size):
    print("*", end="")  # Print asterisk without newline
  print()  # Move to the next line after each row

print("Pattern drawn!")
