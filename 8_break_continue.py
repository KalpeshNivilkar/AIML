i = 1
while i <= 5:
    print(i)
    if i == 3:
        break
    i += 1
print("the loop ends...")
    

# continue 
i = 0
while i <= 10:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1