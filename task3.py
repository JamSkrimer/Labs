a, b = int(input()), int(input())
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
print(math_stuff(a, b, enum))