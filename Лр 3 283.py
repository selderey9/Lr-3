count = 0
prev = int(input("Enter first number:"))
while True:
    curr = int(input("Enter next number:"))
    if curr == 0:
        break
    if prev > curr:
        count += 1
    prev = curr
print(count)

