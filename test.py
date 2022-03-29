def max(pole):
    if len(pole)<1:
        return None
    a = pole[0]
    for i in range(len(pole)):
        if pole[i] > a:
            a = pole[i]
    return a
pole = []
for i in range(-20,2):
    pole.append(i)

print(pole,max(pole))