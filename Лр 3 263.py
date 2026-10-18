while True:
    n = int(input("Enter n(1 - 31):"))
    if n < 1 or n > 31:
        print("Enter valid number:")

    else:
        t = []
        for i in range(n):
            tem = int(input("Temperature:"))
            t.append(tem)
        minimal = min(t)
        print(minimal)
        if minimal < -15:
            print("Yes")
        else:
            print("No")
        break
