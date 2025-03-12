print("Введите минимальную сумму инвестиций")
x = int(input())
print("Сколько денег у майкла?")
a = int(input())
print("Сколько денег у Ивана?")
b = int(input())
if a >= x and b >= x:
    print(2)
elif a >= x > b:
    print("Mike")
elif b >= x > a:
    print("Ivan")
elif a < x <= b + a and b < x:
    print(1)
elif a < x and b < x:
    print(0)
