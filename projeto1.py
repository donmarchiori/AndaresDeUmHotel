print("Usando for:")
for andar in range(20, 0, -1):
    if andar != 13:
        print("Esse é o andar numero: ", andar)

print("\nUsando while:")
andar = 20
while andar >= 1:
    if andar != 13:
        print("Esse é o andar numero: ", andar)
    andar -= 1