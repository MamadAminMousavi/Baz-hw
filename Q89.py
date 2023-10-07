nums=[]
for i in range(10):
    num=int(input())
    
    if num%2==0 or num%3==0:
        if num!=3:
            nums.append(num)

print(nums)