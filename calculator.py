"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

def tokenize_it():
	play_calc = 1
	while play_calc == 1:
		user_input = raw_input("> ") 
		tokens = user_input.split(" ")
		
		if tokens[0] == "+":
			print add(int(tokens[1]),int(tokens[2]))
		
		elif tokens[0] == "-":
			print subtract(int(tokens[1]),int(tokens[2]))
		
		elif tokens[0] == "*":
			print multiply(int(tokens[1]),int(tokens[2]))
		
		elif tokens[0] == "/":
			print divide(float(tokens[1]),float(tokens[2]))
		
		elif tokens[0] == "square":
			print square(int(tokens[1]))
		
		elif tokens[0] == "cube":
			print cube(int(tokens[1]))
		
		elif tokens[0] == "pow":
			print power(int(tokens[1]),int(tokens[2]))
		
		elif tokens[0] == "mod":
			print mod(int(tokens[1]),int(tokens[2]))
		
		elif tokens[0] == "q":
			play_calc = 2
		
		else:
			print "I don't understand that. Please try again."
			print "If you'd like to exit enter q."


#while play_calc == 1:
print "Please only enter two numbers for each arithmetic operation."
tokenize_it()
print "Thank you for using this fantastic calculator. Calc-U-Later!"
