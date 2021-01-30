# Rearrange the code to open a file, read its contents, print them, and then close the file.
file = open("test.txt")
cont = file.read()
print(cont)
file.close()

# How many characters would be in each line printed by this code, if one character is one byte?
file = open("filename.txt", "r")
for i in range(21):
  print(file.read(4))
file.close()
# the number of characters printed each line is 4 characters

# Fill in the blanks to open a file, read its content and print its length.
file = open("filename.txt", "r")
str = file.read()
print(len(str))
file.close()

# If the file test.txt has 7 lines of content, what will the following expression return?
len(open("test.txt").readlines())
# answer = 7
