#1 Develop a python program to Calculate Number of Words
def word_count(s):
    counts = dict()
    words = s.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

print(word_count('the quick brown fox jumps over the lazy dog.'))





#Program 3 WRITE A PYTHON PROGRAM FOR EMAIL SLICER

email = input("Enter Your Email: ").strip()
username = email[:email.index('@')]
domain = email[email.index('@') + 1:]
print(f"Your username is {username} & domain is {domain}")





#Program 5 CREATE A CONTACT LIST USING PYTHON

names = []
phone_numbers = []
num = 3

for i in range(num):
    name = input("Name: ")
    phone_number = input("Phone Number: ")  # For conversion to int => int(input("Phone Number: "))
    names.append(name)
    phone_numbers.append(phone_number)

print("\nName\t\t\tPhone Number\n")
for i in range(num):
    print("{}\t\t\t{}".format(names[i], phone_numbers[i]))

search_term = input("\nEnter search term: ")
print("Search result:")

if search_term in names:
    index = names.index(search_term)
    phone_number = phone_numbers[index]
    print("Name: {}, Phone Number: {}".format(search_term, phone_number))
else:
    print("Name Not Found")





# Program 7 FIBONACCI GENERATOR

# Number of terms to print
n_terms = int(input("How many terms the user wants to print? "))

# First two terms
n_1 = 0
n_2 = 1
count = 0

# Check if the number of terms is valid
if n_terms <= 0:
    print("Please enter a positive integer, the given number is not valid.")
# If there is only one term, it will return n_1
elif n_terms == 1:
    print(f"The Fibonacci sequence of {n_terms} term is:")
    print(n_1)
# Generate Fibonacci sequence for more than one term
else:
    print("The Fibonacci sequence of the numbers is:")
    while count < n_terms:
        print(n_1)
        nth = n_1 + n_2
        # Update values
        n_1 = n_2
        n_2 = nth
        count += 1







#Program 9 DEVELOP A PYTHON PROGRAM TO GENERATE PASSWORD

# Importing the necessary module
import random  # Importing the random module

# Defining a function to randomly generate the password
def generate_password(length):
    """
    This function accepts a parameter 'length' and returns a randomly generated password
    """
    # Defining the list of characters that will be used to generate the password
    list_of_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"

    # Defining an empty password string
    pass_str = ""

    # Creating a loop to randomly select a character from the list and insert it in the
    # password string up to the given length
    for _ in range(length):
        # Using the random.choice() method to select a random character from the list and inserting it in the password string
        pass_str += random.choice(list_of_chars)

    # Returning the generated password string
    return pass_str

# Defining the length of the password
length = 8

# Calling the generate_password() function and storing the returned value in a variable
pass_str = generate_password(length)
# Printing the final result for the users
print("A randomly generated password is:", pass_str)











#Program 11 BUILD A UI CALCULATOR

# Importing the necessary module
import tkinter as tk
from tkinter import messagebox

# Define global variables
var = ""
A = 0
operator = ""

# Create the main application window
root = tk.Tk()
root.title("Calculator")

# Create a StringVar for the display
the_data = tk.StringVar()

# Create the display widget
display = tk.Entry(root, textvariable=the_data, font=('arial', 20, 'bold'), bd=10, insertwidth=4, width=14, justify='right')
display.grid(row=0, column=0, columnspan=4)

# Define button functions
def button_click(num):
    global var
    var = var + str(num)
    the_data.set(var)

def button_clear():
    global var
    global A
    global operator
    var = ""
    A = 0
    operator = ""
    the_data.set(var)

def button_add():
    global A
    global var
    global operator
    A = float(var)
    operator = "+"
    var = var + "+"
    the_data.set(var)

def button_subtract():
    global A
    global var
    global operator
    A = float(var)
    operator = "-"
    var = var + "-"
    the_data.set(var)

def button_multiply():
    global A
    global var
    global operator
    A = float(var)
    operator = "*"
    var = var + "*"
    the_data.set(var)

def button_divide():
    global A
    global var
    global operator
    A = float(var)
    operator = "/"
    var = var + "/"
    the_data.set(var)

def button_equal():
    global A
    global var
    global operator
    var2 = var
    try:
        if operator == "+":
            a = float(var2.split("+")[1])
            x = A + a
        elif operator == "-":
            a = float(var2.split("-")[1])
            x = A - a
        elif operator == "*":
            a = float(var2.split("*")[1])
            x = A * a
        elif operator == "/":
            a = float(var2.split("/")[1])
            if a == 0:
                messagebox.showerror("Division by 0 Not Allowed.")
                A = ""
                var = ""
                the_data.set(var)
                return
            else:
                x = A / a
        the_data.set(x)
        var = str(x)
    except Exception as e:
        messagebox.showerror("Error", str(e))
        button_clear()

# Create buttons and place them in the grid
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0
for button in buttons:
    if button == 'C':
        tk.Button(root, text=button, padx=20, pady=20, font=('arial', 20, 'bold'), command=button_clear).grid(row=row_val, column=col_val)
    elif button == '=':
        tk.Button(root, text=button, padx=20, pady=20, font=('arial', 20, 'bold'), command=button_equal).grid(row=row_val, column=col_val)
    elif button in {'+', '-', '*', '/'}:
        command = {
            '+': button_add,
            '-': button_subtract,
            '*': button_multiply,
            '/': button_divide
        }[button]
        tk.Button(root, text=button, padx=20, pady=20, font=('arial', 20, 'bold'), command=command).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=button, padx=20, pady=20, font=('arial', 20, 'bold'), command=lambda num=button: button_click(num)).grid(row=row_val, column=col_val)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Start the main event loop
root.mainloop()






#Program 14 WRITE A PYTHON PROGRAM FOR NUMBER GUESSING

import random
import math

# Taking Inputs
lower = int(input("Enter Lower bound: "))
upper = int(input("Enter Upper bound: "))

# Generating a random number between the lower and upper bounds
x = random.randint(lower, upper)
print(f"\n\tYou've only {round(math.log(upper - lower + 1, 2))} chances to guess the integer!\n")

# Calculating the maximum number of guesses allowed
max_attempts = round(math.log(upper - lower + 1, 2))

# Initializing the number of guesses
count = 0

while count < max_attempts:
    # Taking the guessing number as input
    guess = int(input("Guess a number: "))

    # Condition testing
    if x == guess:
        print(f"Congratulations you did it in {count + 1} tries!")
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You guessed too high!")

    # Incrementing the guess count
    count += 1

# If guessing attempts are exhausted, show this output
if count >= max_attempts:
    print(f"\nThe number was {x}")
    print("\tBetter Luck Next time!")
    print(f"\n\tYou've only {max_attempts} chances to guess the integer!\n")





