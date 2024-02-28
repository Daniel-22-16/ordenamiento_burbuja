#cear una funcion de para el algoritmo burbuja sonbre una lista

def ordenamiento_burbuja(lista):
    for n in range(len(lista) -1, 0, -1):
        for i in range(n):
            if lista[i] > lista[i + 1]:
                temp = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = temp


numeros =[7, 19, 23, 13,  5, 29, 2, 11, 17]
print(numeros)

ordenamiento_burbuja(numeros)
print(numeros)