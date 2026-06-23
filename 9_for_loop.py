# for loop... 
# Print the elements of the following list using a loop:

# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

'''nums = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
for i in nums:
    print(i)
    i += 1'''

# Search for a number x in this tuple using loop:

# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

'''nums = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
x = 25
for i in nums:
    if i == 25:
        print(i,"this is x value")
        break
    else:
        print(i)
        i+= 1'''


# find character in string 
'''str1 = "apnacollege"
for i in str1:
    if i == 'o':
        print("o is found")
        break
    else:
        print(i)'''

# even number usnig help of range 
'''for i in range(0,10,2):
    print("even num:",i)'''

# Print numbers from 1 to 100.
'''for i in range(0,101):
    print(i)'''

# Print numbers from 100 to 1.
# for i in range(100,0,-1):
#     print(i)

# Print the multiplication table of a number n.
'''for i in range(1,11):
    print(i*2)'''

# wap to find factorials 
n= 10
fact = 1
for i in range(1,10):
    fact *= i
print(fact)



