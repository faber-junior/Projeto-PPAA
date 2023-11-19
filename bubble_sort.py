lista = [12, 25, 10, 98, 26, 2, 1, 15]

tam_lista = len(lista)

troca = False

for i in range(tam_lista):
    troca = False
    for n in range(tam_lista - 1):
        if lista[n] > lista[n + 1]:
            lista[n], lista[n + 1] = lista[n + 1], lista[n]
            troca = True
        print(lista)
    if troca == False:
        break
    print()