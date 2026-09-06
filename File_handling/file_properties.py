# this is file properties tutorials
f = open("sample.txt","r")
print("File name:",f.name)
print("file mode:", f.mode)
print("Is file closed", f.closed)
f.close()
print("Is file closed:", f.closed)

