lista = [12, 25, 10, 98, 26, 2, 1, 15]

tam_lista = len(lista)

for i in range(tam_lista):
    for j in range(i, 0, -1):
        if lista[j] < lista[j - 1]:
            lista[j], lista[j - 1] = lista[j - 1], lista[j]
    print(lista)