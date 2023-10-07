
num1 = input()
num2 = input()

if len(num1) == 3 and len(num2) == 3:
        sum = bin(int(num1,2)+int(num2,2))[2:]

print(sum)