import random
def array(size=8):
    even_numbers = list(range(2, 101, 2))
    return sorted(random.sample(even_numbers, min(size, len(even_numbers))))
print(f"Массив: {array(random.randint(5, 10))}")