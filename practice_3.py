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

student_dict = {}
for student,subject in info:
    if student not in student_dict:
        student_dict[student] = [subject]
    else:
        student_dict[student] += [subject]
print(student_dict)
