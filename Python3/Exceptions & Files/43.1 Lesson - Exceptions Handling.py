# What is the output of this code?
try:
  variable = 10
  print (10 / 2)
except ZeroDivisionError:
  print("Error")
print("Finished")

# output = 5.0 Finished


# What is the output of this code?
try:
  meaning = 42
  print(meaning / 0)
  print("the meaning of life")
except (ValueError, TypeError):
  print("ValueError or TypeError occurred")
except ZeroDivisionError:
  print("Divided by zero")

# output = Divided by zero


# Fill in the blanks to handle all possible exceptions.
try:
  num1 = input(":")
  num2 = input(":")
  print(float(num1)/float(num2))
except:
	print("Invalid input")
