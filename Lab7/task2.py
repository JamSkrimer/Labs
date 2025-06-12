import random
nums = [random.randint(-100, 100) for i in range(20)]
positive = []
for i in nums:
    if i > 0:
        positive.append(i)
print(positive)