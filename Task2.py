import random
list = []
a = 0
for i in range(14):
    i = int(input("Enter a number: "))
    a = a + i
    list.append(i)
list.append(a)
for a in list:
    print(a)