nums = []
for i in range(100):
    num = int(input())
    nums.append(num)
    
f1 = 0
f2 = 1
sum = 0

for i in nums:
    if i % 2 == 1:
        while f2 < i:
            fsum = f1 + f2
            f1 = f2
            f2 = fsum
        if f2 == i:
            sum += 1

print(sum)
