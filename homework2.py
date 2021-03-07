def Fib():
    f0, f1 = 0, 1
    while True:
        yield f0
        f0, f1 = f1, f0 + f1


fib_list = []

num = int(input('Insert a Number: '))

for a in Fib():
    fib_list.append(a)
    if a > num - 8:
        Sum = sum(fib_list)
        break

print(Sum)

if num > 1:

    for i in range(2, int(num / 2) + 1):

        if (num % i) == 0:
            print("The number", num, "is NOT a prime number")
            break
    else:
        print("The number", num, "IS a prime number ")

else:
    print("The number", num, "is NOT a prime number")

def Binary(n):

   if n > 1:

       Binary(n//2)

   print(n % 2 , end = '')

decimal = num

Binary(decimal)
print()