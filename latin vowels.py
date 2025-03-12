a = input()
counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
counter5 = 0
counter6 = 0
for i in a:
    if i == "a":
        counter1 += 1
    elif i == "e":
        counter2 += 1
    elif i == "i":
        counter3 += 1
    elif i == "o":
        counter4 += 1
    elif i == "u":
        counter5 += 1
    else:
        counter6 += 1

print("Согласных букв -", counter6)
print("Гласных букв -", counter1+counter2+counter3+counter4+counter5)
if counter1 > 0:
    print("a", counter1)
else:
    print("a", False)

if counter2 > 0:
    print("e", counter2)
else:
    print("e", False)

if counter3 > 0:
    print("i", counter3)
else:
    print("i", False)

if counter4 > 0:
    print("o", counter4)
else:
    print("o", False)
if counter5 > 0:
    print("u", counter5)
else:
    print("u", False)




