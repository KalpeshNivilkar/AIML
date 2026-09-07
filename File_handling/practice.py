'''data = True
word = "python"
line = 1

with open("sample.txt","r") as f:
    while data:
        data = f.readline()
        if word in data:
            print(f"{word} is found in line no :{line}")
            break
        line += 1'''


'''with open("Sample.txt","r") as f:
    data = f.readline()
    line = 1

    while data:
        if "python" in data.lower():
            print(f"word found at {line} line")
            break
        data = f.readline()
        line += 1
'''

# Q1
# . Create a program that:
# 1. Opens a file  
# "names.txt"
# in write mode
# 2. Writes 5 names (one per line) entered by the user
# 3. Then opens the same file in read mode and prints all names

'''with open("sample.txt","w") as f:
    for i in range(5):
        name = input(f"enter the name {i+1}:")
        f.write(name + "\n")

with open("sample.txt","r") as f:
    data = f.read()
    print(data)'''

# Q2
# . Create a program that:
# 1. Opens a file  
# "log.txt"
# in append mode
# 2. Adds a new log entry (like "Program run successfully")
# 3. Opens the file in read mode and prints all logs
    
'''with open("log.txt","a") as f:
    f.write("\nprogram run successfully")

with open("log.txt","r") as f:
    data = f.read()
    print(data)'''



