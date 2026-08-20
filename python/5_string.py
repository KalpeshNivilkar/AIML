# practice:
'''# WAP to input user’s first name & print its length.
name = input("enter your name: ")
name_lenght = len(name)
print(name_lenght)'''

# WAP to find the occurrence of ‘$’ in a String.
'''str = "knksnsk$KNK$NK$N$N$KN$KN$KN$N"
str_count = str.count("$")
print(str_count)'''

# Write a program that asks the user for their first name and last name, then prints a sentence like:
'''first_name = input("enter your first name: ")
last_name = input("enter your last name:")
greet_msg = "welcome to pyhton tutorials!"
concatenation_str = first_name +" "+ last_name+" "+ greet_msg
print(concatenation_str)'''

# Take a string as input from the user and print:

# Total number of characters
# First character
# Last character

'''str_input = input("enter str:")
length_str = len(str_input)
first_ch = str_input[0]
last_ch = str_input[-1]
print(length_str,first_ch,last_ch)'''

# Ask the user to enter a sentence. Convert and print it in:

# UPPERCASE
# lowercase
# Title Case

'''str_input = input("enter the str: ")
uppercase_str = str_input.upper()
lowercase_str = str_input.lower()
title_str = str_input.title()
print(uppercase_str,lowercase_str,title_str)'''


# The user enters a string containing leading and trailing spaces (e.g., " Python Programming ").

# Perform the following operations:

# Remove extra spaces
# Print the cleaned string
# Print its length before and after removing spaces

'''s = " Python Programming "
old_length = len(s)
new_S = s.strip()
new_length = len(new_S)
print(new_S,old_length,new_length)'''


# Q5.

# Take a word as input and print:

# The original word
# The reversed word

'''word = input("enter:")
rev_word = word[::-1]
print(word,rev_word)'''

# Ask the user to enter a sentence. Convert the sentence into a list of words and print the total number of words.

'''user = input("sentence: ")
words = user.split()
print(words)'''

# Q9.

# Ask the user to enter an email address. Check whether it contains the "@" symbol.

# If present, print "Valid format".
# Otherwise, print "Invalid format".


'''email = input("enter your email: ")
if "@" in email:
    print("valid format.")
else:
    print("invalid format.")'''
