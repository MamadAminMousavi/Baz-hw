n = int(input())
num = []

for i in range(n):
    number = int(input())
    num.append(number)


numsort = sorted(num)

if num == numsort:
    print("yes")
else:
    print("no")