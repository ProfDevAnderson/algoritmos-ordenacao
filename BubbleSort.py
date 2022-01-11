lista = [9, 5, 2 , 35,6, 1, 10, 85, 99, 4, 3]

n = len(lista)
for j in range(n-1):
    for i in range(n-1):
        if lista[i] > lista[i+1]:
           lista[i],lista[i+1] = lista[i+1],lista[i]
print(lista)

# O(n²)