# Which number is not printed by this code?
try:
  print(1)
  print(20 / 0)
  print(2)
except ZeroDivisionError:
  print(3)
finally:
  print(4)
# answer = 2

# Open the file in binary write mode.
open("test.txt", "wb")

# Fill in the blanks to try to open and read from a file. Print an error message in case of an exception.
try:
	with open("test.txt") as f:
	print(f.read())
except:
	print("Error")

# What is the highest number that would be printed by this code?
try:
  print(1)
  assert 2 + 2 == 5
except AssertionError:
  print(3)
except:
  print(4)
# the highest number that would be printed is 3
