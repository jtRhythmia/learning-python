# Name: Joshua Tan

print("It worked!")

x = None

example = "Im a string" # The variable called [example] is now holding the [string] value ["I'm a string!"]
a = 3 # The variable called [a] is now holding the [integer] value [3]
b = 4.0 # The variable called [b] is now holding the [float] value [4.0]
c = True # The variable called [c] is now holding the [Boolean] value [True]
d = False # The variable called [d] is now holding the [Boolean] value [False]
e = "Hey!" # The variable called [e] is now holding the [string] value ["Hey!"]
f = None # The variable called [f] is not holding any value
age = 32 # The variable called [age] is now holding the [integer] value [32]
name = "Josh" # The variable called [name] is now holding the [string] value ["Josh"]
instrument = "Drums" # The variable called [name] is now holding the [string] value ["Drums"]

'''
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _)
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.

'''


# prompt = "Enter your name"
# response = input(prompt)
# print("Hello,", response)
# print(response, ", here is your agenda for the day...")




# prompt_one = "Enter your name:"
# response_one = input(prompt_one)

# prompt_two = "Enter your age:"
# response_two = input(prompt_two)

# print(response_one, type(response_one))
# print(response_two, type(response_two))

# Problem 2
# Ask the user for the two numbers
# first_number = input("What's the first number?")
# second_number = input("What's the second number?")

# Convert the numbers to integer versions of themselves
# first_number = int(first_number)
# second_number = int(second_number)

# Compare the two numbers
# if first_number > second_number:
#     print(first_number, "is bigger.")

# elif first_number == second_number:
#     print("The numbers are equal")

# else:
#     print(second_number, "is bigger.")

# Problem 5
# Ask the user for their name and save in variable called "name"
name = input("What's your full name?")
while " " in name:
    name = name.replace(" ", "")
    
# Calculate the length of name
length_of_name = len(name)

# Print the length
print(length_of_name)




