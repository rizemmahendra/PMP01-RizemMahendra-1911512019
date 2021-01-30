# Will the close() function get called in this code?
try:
  f = open("filename.txt")
  print(f.read())
  # print(1 / 0)
finally:
  f.close()
# answer = Yes

# Fill in the blanks to create a valid with statement, reading the contents of the file.
with open("test.txt") as f:
  print(f.read())
