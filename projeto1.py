print("Usando for:")
for andar in range(20, 0, -1):
    if andar != 13:
        print(andar)

print("\nUsando while:")
andar = 20
while andar >= 1:
    if andar != 13:
        print(andar)
    andar -= 1