a, b = int(input()), int(input())

def calc(first, second):
    return (first + 4*second) * (first - 3*second) + first**2
print(calc(a, b))
