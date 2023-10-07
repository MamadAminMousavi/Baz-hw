num1 = int(input())
week = 0
if 1<= num1 <=30:

    if num1 >= 1 and num1 <= 7:
        week = 1

    elif num1 >= 8 and num1 <= 14:
        week = 2

    elif num1 >= 15 and num1 <= 21:
        week = 3

    elif num1 >= 22 and num1 <= 28:
        week = 4

    elif num1 >= 29 and num1 <= 30:
        week = 5

print(week)