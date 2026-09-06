data = True
word = "python"
line = 1

with open("sample.txt","r") as f:
    while data:
        data = f.readline()
        if word in data:
            print(f"{word} is found in line no :{line}")
            break
        line += 1