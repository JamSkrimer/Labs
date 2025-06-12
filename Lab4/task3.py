try:
    print("Enter two numbers")
    a, b = int(input()), int(input())
except:
    print("these ain't numbers")
    exit()
enum = str(input())
def math_stuff(q, p, oper):
    if enum == "+":
        result = q + p
    if enum == "-":
        result = q - p
    if enum == "*":
        result = q * p
    if enum == "/":
        result = q / p
    return result
try:
    print(math_stuff(a, b, enum))
except:
    print("use actually existing commands. try again")
    print(math_stuff(a, b, enum))