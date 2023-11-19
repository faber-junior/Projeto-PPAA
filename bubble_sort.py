lista = [12, 25, 10, 98, 26, 2, 1, 15]

tam_lista = len(lista)

for i in range(tam_lista):
    for n in range(tam_lista - 1):
        if lista[n] > lista[n + 1]:
            lista[n], lista[n + 1] = lista[n + 1], lista[n]
        print(lista)
    print()