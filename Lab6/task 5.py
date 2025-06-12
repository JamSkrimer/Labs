c = "C"
A = ["CaaaC", "sus", "C", "COOL", "COOLREALLYCOOLC"]
amount = 0
for i in A:
    if len(i) > 1 and i.startswith(c) and i.endswith(c):
        print(i)
        amount += 1
print(amount)