
def merge(A, p, q, r):
    izquierda = A[p:q+1]
    derecha = A[q+1:r+1]

    izquierda.append(float("inf"))
    derecha.append(float("inf"))
   

    i = 0
    j = 0
    k = p

    while k <= r and j < len(derecha) and i < len(izquierda):
        if izquierda[i]>derecha[j]:
            A[k] = derecha[j]
            j+=1
        else:
            A[k] = izquierda[i]
            i+=1
            k+=1

   



def mergeSort(A, p, r):
    if p < r:
      
        q = (p + r)//2
        mergeSort(A, p, q)
        mergeSort(A, q+1, r)
        merge(A, p, q, r)



