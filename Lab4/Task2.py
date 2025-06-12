import random
list = []
a = 0
for i in range(14):
    try:
        i = int(input("Enter a number: "))
    except:
        print("this is not a number")
    a = a + i
    list.append(i)
list.append(a)
for a in list:
    print(a)