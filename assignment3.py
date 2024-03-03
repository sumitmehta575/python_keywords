#1.Explain the significance of Python keywords and provide examples of five keywords.
x = 10
if x > 5:
    print("x is greater than 5")

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

i = 1
while i <= 5:
    print(i)
    i += 1

def greet(name):
    print("Hello, " + name + "!")

def add(x, y):
    return x + y

result = add(3, 5)
print(result)

#2.Describe the rules for defining identifiers in Python and provide an example.

# Valid identifiers
my_variable = 10
MyClass = 5
another_variable_2 = "Hello"

# Invalid identifiers
3variable = 7   # Identifier cannot start with a digit
if = 5          # 'if' is a keyword, cannot be used as an identifier
my-variable = 8 # Hyphens are not allowed in identifiers

#3.What are comments in Python, and why are they useful ? Provide an example.

# This is a single-line comment in Python

# This program calculates the sum of numbers from 1 to 10
sum = 0

# Loop through numbers from 1 to 10 and add them to the sum
for i in range(1, 11):
    sum += i  # This line adds the current number 'i' to the sum

# Print the final sum
print("The sum of numbers from 1 to 10 is:", sum)

#4.Why is proper indentation important in Python.

# Incorrect indentation
if True:
print("This line is not properly indented")

# Correct indentation
if True:
    print("This line is properly indented")

#5.What happens if indentation is incorrect in Python.

# Incorrect indentation
if True:
print("This line is not properly indented")

#6.Differentiate between expression and statement in Python with examples.

# Expression example
x = 5 + 3  # Here, '5 + 3' is an expression that evaluates to 8
print(x)   # 'print(x)' is also an expression, but it's used as a statement

# Statement example
if x > 5:  # 'if' statement, evaluating an expression 'x > 5'
    print("x is greater than 5")  # 'print()' statement inside the 'if' block
else:
    print("x is not greater than 5")

