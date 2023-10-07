num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 >= num2 and num2 >= num3:
    max = num1
    med = num2
    min = num3

elif num1 >= num3 and num3 >= num2:
    max = num1
    med = num3
    min = num2

elif num2 >= num1 and num1 >= num3:
    max = num2
    med = num1
    min = num3

elif num2 >= num3 and num3 >= num1:
    max = num2
    med = num3
    min = num1

elif num3 >= num1 and num1 >= num2:
    max = num3
    med = num1
    min = num2

else:
    max = num3
    med = num2
    min = num1

print(max,med,min)