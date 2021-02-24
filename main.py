def Fib():
    f0, f1 = 0, 1
    while True:
        yield f0
        f0,f1 = f1, f0 +f1

fib_list = []

num = int(input('INsert Your Age Here '))

for a in Fib():
    fib_list.append(a)
    if a > num - 8:
        Sum = sum(fib_list)
        break

print(Sum)
print(Arti)
