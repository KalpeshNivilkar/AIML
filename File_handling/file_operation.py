'''f = open("sample.txt","r")
data = f.readline()
print(data)

f = open("sample.txt", "w")
data = f.write("this is my new file ")
print(data)
f.close()'''

'''# append
f = open("sample.txt","a")
data = f.write(" this is append text.")'''

# x Modu 
'''f = open("sample2.txt","x")
data = f.write("this is new file using x mode")'''



'''f = open("sample.txt","r+")
data = f.read()
f.write("I am from raigad.")

print(data)'''

'''f = open("sample2.txt","a+")
f.write(" this is last line")
f.seek(0)  
print(f.read())
f.close()'''

f = open("simple.txt","r+")
f.seek(0)
print(f.read())