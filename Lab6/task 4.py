import random
nums = [random.randint(-100, 100) for i in range(20)]
positive = []
negative = []
for i in nums:
    if i < 0:
        negative.append(i)
    elif i > 0:
        positive.append(i)
print(nums)
print(positive[1])
print(negative[-1:])