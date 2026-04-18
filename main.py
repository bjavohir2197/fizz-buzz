def chiqar_3_5ga_bo_linadiganlar(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print(i)

n = int(input("Sonni kiriting: "))
chiqar_3_5ga_bo_linadiganlar(n)
