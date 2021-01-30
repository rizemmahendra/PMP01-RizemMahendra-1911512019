# Which errors occur during the execution of this code?
try:
	print(1 / 0)
except ZeroDivisionError:
	raise ValueError
# error during execution this code is ZeroDivisionError and ValueError

# Fill in the blanks to raise a ValueError exception, if the input is negative.
num = input(":")
if float(num) < 0:
	raise ValueError("Negative!")

# Can you use the raise statement outside the except block?
# answer = Yes
