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


with open("Sample.txt","r") as f:
    data = f.readline()
    line = 1

    while data:
        if "python" in data.lower():
            print(f"word found at {line} line")
            break
        data = f.readline()
        line += 1


