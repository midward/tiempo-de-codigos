//midward brayan lipa quispe
//comparacion de tiempos
from timeit import timeit

inicializacion = 'from math import sqrt'
codigo = '''
raices = []
for i in range(100):
    raices.append(sqrt(i))
'''

print(timeit(setup=inicializacion, stmt=codigo, number=10000))

codigo = '''
raices = []
raices = [lambda i: sqrt(i) for i in range(100)]
'''

print(timeit(setup=inicializacion, stmt=codigo, number=10000))

print()



codigo_seleccion = '''
A = [64, 25, 12, 22, 11] 

for i in range(len(A)):
    min_idx = i
    for j in range(i+1, len(A)):
        if A[min_idx] > A[j]:
            min_idx = j

    A[i], A[min_idx] = A[min_idx], A[i]
'''

codigo_insercion = '''
arr = [64, 25, 12, 22, 11]
for i in range(1, len(arr)): 

    key = arr[i] 

    j = i-1
    while j >=0 and key < arr[j] : 
            arr[j+1] = arr[j] 
            j -= 1
    arr[j+1] = key
'''
codigo_burbuja = '''
A = [64, 25, 12, 22, 11] 

for i in range(1,len(A)):
        for j in range(0,len(A)-i):
            if(A[j+1] < A[j]):
                aux=A[j];
                A[j]=A[j+1];
                A[j+1]=aux;
'''
codigo_sort = '''
data = [64, 25, 12, 22, 11]
for value in data:
        counts[value] += 1
    print(counts)    
 

    for index in range(1, len(counts)):
        counts[index] = counts[index-1] + counts[index]
    print(counts)

    arr = [0 for loop in range(len(data))]
    for value in data:
        index = counts[value] - 1
        arr[index] = value
        counts[value] -= 1
 

'''
print("ordenamiento seleccion")
print(timeit(stmt=codigo_seleccion, number=1000000))
print("ordenamiento insercion")
print(timeit(stmt=codigo_insercion, number=1000000))
print("ordenamiento burbuja")
print(timeit(stmt=codigo_burbuja, number=1000000))
print("ordenamiento counting sort ")
print(timeit(stmt=codigo_burbuja, number=1000000))
