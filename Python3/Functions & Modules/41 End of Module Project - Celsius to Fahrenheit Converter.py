"""
Celsius to Fahrenheit

You are making a Celsius to Fahrenheit converter.
Write a function to take the Celsius value as an argument and return the corresponding Fahrenheit value.
"""

celsius = int(input())

def conv(c):
    #your code goes here
    result = 9/5 * c + 32
    return result

fahrenheit = conv(celsius)
print(fahrenheit)
