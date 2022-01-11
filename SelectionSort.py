# Selection Sort
lista = [9, 5, 2 , 35,6, 1, 10, 85, 99, 4, 3]

n = len(lista)
for j in range(n-1):
    minino_index = j
    for i in range(j, n):
        if lista[i] < lista[minino_index]:
            minino_index = i
    if lista[j] > lista[minino_index]:
        aux = lista[j]
        lista[j] = lista[minino_index]
        lista[minino_index] = aux
# O(n²)
# 1 + 5*(n-1) + X*(n-1)
# 1 + 5*(n-1) + (n²+n-2)/2
# (1 - 5) | (5n + n/2) | (n²/2)
# (5n + n/2) = 5500
# n²/2 = 500000