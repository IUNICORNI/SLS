a = int(input())
b = int(input())
counter = 0
for i in range(a, b+1):
    if i % 2 == 0:
        counter += 1
print(counter)
