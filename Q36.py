num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 >= num2 and num1 >= num3:
    max = num1
elif num2 >= num1 and num2 >= num3:
    max = num2
else:
    max = num3

print(max)