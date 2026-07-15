info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English")
]

# print the unique subject only 

'''list_sub = set()
for el in info:
    sub = el[1]
    list_sub.add(sub)
print(list_sub)'''

# output : {'English', 'Math', 'Science'}

# list student enrolled in english 

'''student_list = []
for name, subject in info:
    if subject == "English":
        student_list.append(name)
    
print(student_list)'''

# output : ['Alice', 'Charlie']

# create dict student and set of cource 

'''student_dict = {}
for student,subject in info:
    if student not in student_dict:
        student_dict[student] = [subject]
    else:
        student_dict[student] += [subject]
print(student_dict)'''

# output : {'Alice': ['Math', 'Science', 'English'], 'Bob': ['Science', 'Math'], 'Charlie': ['Math', 'English']}


# Q1
# . Ask the user for a string and check whether it is a palindrome or not. 
# A  
# palindrome
# “madam”, “
# is a string which is same when we read it forward & backward. Eg - 
# racecar” etc.
# [ 
# Hint- A palindrome string is equal to the reversed version of the string. We can 
# use a loop to reverse the string manually. ]


'''def is_palindrome(s):
    og_s = s
    rev_s = s[::-1]

    if rev_s == og_s:
        return True
    return False
s = "madam"
print(is_palindrome(s))'''

# using two pointer 

'''def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
s = "madam"
print(is_palindrome(s))'''

# output : True 

# Given a list of integers compute the average of all numbers in the list.

'''list = [10,10,10]
total  = 0
n =len(list)
for i in list:
    total += i
avg = total / n
print(avg)'''

'''nums = list(map(int,input("enter a numbers").split()))
total = 0
for num in nums:
    total += num
avg = total / len(nums)
print(avg)'''

#  Input two lists of integers from the user. Merge them into one list and sort the 
# result.
# Eg -  
# list1 = [1, 2, 7]
# ,  
# list2 = [2, 4, 5]
# result = [1, 2, 3, 54, 5, 7]

# list_1 = []
# list_2 = []
# list_3 = []
# n = int(input("how many time you have to take an input:"))
# for i in range(n):
#     i = int(input("enter a number:"))
#     list_1.append(i)

# for j in range(n):
#     j = int(input("enter a number:"))
#     list_2.append(j)
# print(list_1)
# print(list_2)

# list_3.append(list_1,list_2)

'''numbers1 = list(map(int, input("Enter numbers: ").split()))
numbers2 = list(map(int, input("Enter numbers: ").split()))
for num in numbers2:
    numbers1.append(num)
print(sorted(numbers1))'''


# . Given a tuple of integers, create:
# A tuple of all even numbers
# A tuple of all odd numbers

'''nums = (2,3,4,5,6,7,8,9)
even_num = ()
odd_num = ()
for num in nums:
    if num % 2 == 0:
        even_num += (num,)
    else:
        odd_num += (num,)
print(f"even num :{even_num}")
print(f"odd num : {odd_num}")'''

#  Create a dictionary where:
# Q5
# Q6
# • 
# Keys = student names
# • 
# Values = marks (integer)
# A
# Write a menu-based program where user presses a key (ʼAʼ, ‘Bʼ, ‘Cʼ, ‘Dʼ) 
# depending on the operation they want to perform on the dictionary:
# 1. - Add a student
# B
# 2. - Update marks
# C
# 3. - Search for a student
# D
# 4. - Display all students and marks

'''student_hash_table = {}

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("A. Add Student")
    print("B. Update Marks")
    print("C. Search Student")
    print("D. Display All Students")
    print("E. Exit")

    user_input = input("Enter your choice: ").upper()

    # Add Student
    if user_input == 'A':
        print("\n--- Add Student ---")

        student_name = input("Enter student name: ")
        student_marks = int(input("Enter student marks: "))

        if student_name not in student_hash_table:
            student_hash_table[student_name] = student_marks
            print("Student added successfully!")
        else:
            print("Student already exists!")

    # Update Marks
    elif user_input == 'B':
        print("\n--- Update Marks ---")

        student_name = input("Enter existing student name: ")

        if student_name not in student_hash_table:
            print("Student not found!")
        else:
            updated_marks = int(input("Enter updated marks: "))
            student_hash_table[student_name] = updated_marks
            print("Marks updated successfully!")

    # Search Student
    elif user_input == 'C':
        print("\n--- Search Student ---")

        student_name = input("Enter student name: ")

        if student_name not in student_hash_table:
            print("Student not found!")
        else:
            print("Name :", student_name)
            print("Marks:", student_hash_table[student_name])

    # Display All Students
    elif user_input == 'D':
        print("\n--- Student Records ---")

        if len(student_hash_table) == 0:
            print("No student records found.")
        else:
            for student_name, student_marks in student_hash_table.items():
                print(student_name, ":", student_marks)

    # Exit
    elif user_input == 'E':
        print("Thank you!")
        break

    # Invalid Choice
    else:
        print("Invalid Choice!")'''

# Given a list of words:
# words = ["apple", "banana", "kiwi", "cherry", "mango"]
# Create a dictionary that maps each word to its length.
# Example:
# {"apple": 5, "banana": 6, "kiwi": 4, ...

'''words = ["apple", "banana", "kiwi", "cherry", "mango"]
hash_table = {}
for fruit in words:
    word_length = (len(fruit))
    hash_table[fruit] = word_length

print(hash_table)'''

# Write a program that takes a string from the user and prints the number of 
# spaces in the string.

sen = input("enter the string: ")
print(sen.count(" "))


    



