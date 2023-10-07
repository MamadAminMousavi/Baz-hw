def sort():
    n = int(input())
    num = []

    for i in range(n):
        number = int(input())
        num.append(number)

    num.sort(reverse=True)
    print(num)


sort()