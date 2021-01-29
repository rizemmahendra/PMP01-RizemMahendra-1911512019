# What is the output of this code?
def shout(word):
   return word + "!"
speak = shout
output = speak("shout")
print(output)
# output = shout!

# Fill in the blanks to pass the function "square" as an argument to the function "test":
def square(x):
	return x * x

def test(func, x):
	print(func(x))

test(square, 42)
