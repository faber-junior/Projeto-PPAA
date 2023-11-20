lista = [12, 25, 10, 98, 26, 2, 1, 15]

tam_lista = len(lista)

print(lista)

for i in range(tam_lista):
    menor = i
    for j in range(i + 1, tam_lista):        
        if lista[j] < lista[menor]:
            menor = j
    lista[i], lista[menor] = lista[menor], lista[i]
    print(lista)
    