n = int(input())
num = []

for i in range(n):
    number = int(input())
    num.append(number)

max = num[0]

for i in num:
    if i > max:
        max = i

print(max)