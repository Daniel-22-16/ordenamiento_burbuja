def ordenamiento_burbuja(lista):
    for n in range(len(lista) -1, 0, -1):
        for i in range(n):
            if lista[i] > lista[i + 1]:
                temp = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = temp

numeros = [15, 18, 13, 25, 10, 9, 5, 3]
print(numeros)

ordenamiento_burbuja(numeros)
print(numeros)