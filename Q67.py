num = int(input())

f1 = 0
f2 = 1

sum = 0


while f2 <= 100000:
    if f2 % num == 0:
        print(f2)
    fsum = f1 + f2
    f1 = f2
    f2 = fsum