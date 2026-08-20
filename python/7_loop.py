# Print numbers from 1 to 100.
'''for i in range(1,100):
    print(i)'''
'''i = 1
while i < 101:
    print(i)
    i += 1'''

# print 100 to 1 N 
'''i = 100
while i > 0:
    print(i)
    i -= 1'''



# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
'''my_list = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
for i in my_list:
    print(i)'''


# Search for a number x in this tuple using loop:

# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
'''my_list = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
for i in my_list:
    if i == 25:
        print(i)'''

# Print the multiplication table of a number n.
'''n = int(input("enter the number:"))
for i in range(1,11):
    print(i* n)'''

# WAP to find the sum of first n numbers. (using while)

n = 5
sum = 0
for i in range(1,n+1):
    sum += i
    
print(sum)
