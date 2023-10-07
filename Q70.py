for num in range(56,1985):
    for i in range(1,num + 1):
        if num % i == 0:
            print(f"{num} = {i}")