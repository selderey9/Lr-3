n = int(input("Enter a number (>0):"))
numbers = list(map(int, str(n)))
dif = max(numbers) - min(numbers)
if dif % 2 == 0:
    print("Yes")
else:
    print('No')
