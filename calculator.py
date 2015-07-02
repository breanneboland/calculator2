"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here

def split_number_strings(string):
    """
    This function splits the raw input string into two or three separate strings.

    It uses the space as the splitting cue.
    """    
    token_list = string.split(" ")
    return token_list


def calculate_numbers():
    """
    This function takes the list of tokens and sorts them through the different operations.
    """
    while True:

        string = raw_input("Enter your operand and then one or two numbers, as appropriate. > ")

        token_list = split_number_strings(string)

        num1 = None
        num2 = None

        operand = token_list[0]
        if len(token_list) > 1:
            num1 = int(token_list[1])
        if len(token_list) > 2:
            num2 = int(token_list[2])

        if num2 == None:
            if operand == "square":
                print square(num1)
            elif operand == "cube":
                print cube(num1)
            else: 
                print "You need two numbers for that, friend."
        if num2 != None:
            pass:
                if operand == "+":
                    print add(num1, num2)
                elif operand == "-":
                    print subtract(num1, num2)
                elif operand == "*":
                    print multiply(num1, num2)
                elif operand == "/":
                    print divide(num1, num2)
                elif operand == "pow":
                    print power(num1, num2)
                elif operand == "mod":
                    print mod(num1, num2)


        elif operand == "q":
            break
        else:
            print "Yeah, no."


calculate_numbers()