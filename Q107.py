
def nums(num1, num2, num3, num4, num5):
    numbers = [num1, num2, num3, num4, num5]
    average = (num1 + num2 + num3 + num4 + num5) / 5
    num = []

    for i in numbers:
        if abs(i - average) >= 3:
            num.append(i)

    if len(num) > 0:
        return num


num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())

num = nums(num1, num2, num3, num4, num5)
print(num)