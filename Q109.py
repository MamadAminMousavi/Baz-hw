def fa():
    num = int(input())

    for i in range(num):
        number = int(input())
        result = 1
        for m in range(1, number+1):
            result *= m
        print(f"{number} != {result}")


fa()