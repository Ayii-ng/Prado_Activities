# Using + Concatenate Strings in Python using 4 variables concatenate them with spaces

greet = "Hi"
firstName = "Iris"
pronoun1 = "I"
pronoun2 = "am"

result1 = greet + ', ' + pronoun1 + ' ' + pronoun2 + ' ' + firstName
print(result1)

# Using + Concatenate Strings in Python get two strings from user input and concatenate them

textInput_1= input("Enter your Class Year: ")
textInput_2 = input("Enter your Class Section: ")

result2 = textInput_1 + " " + textInput_2

print(result2)

# Using + Concatenate in Python using your name and your age in a paragraph

name = "Iris"
age = 20

result3 = "Hello, I am " + name + " and I am " + str(age) + ". Nice to meet you!"

print(result3)

# Create a Python program to perform Addition Subtraction Multiplication and Division using two numbers

print("please enter a value to perform an Addition, Subtraction, Multiplication & Addition")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

add = num1 + num2
sub = num1 - num2
multipli = num1 * num2
divide = num1 / num2
divi = num1 // num2 

print("sum: ", add)
print("difference: ", sub)
print("product: ", multipli)
print("quotient: " + str(divide) + " Without Decimal: " + str(divi))