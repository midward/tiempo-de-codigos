import insertionsort
import mergesort
import Burbuja
import Seleccion
import numpy
import time

for size in [10,50,100,500,1000]:
    for i in range(0,6):
        listaA = numpy.random.randint(1,1000,size).tolist()
        listaB = numpy.random.randint(1,1000,size).tolist()
        listaC = numpy.random.randint(1,1000,size).tolist()
        listaF = numpy.random.randint(1,1000,size).tolist()
        
        

        inicioInsertion =time.time()
        insertionsort.insertionSort(listaA)
        finalInsertion = time.time()
        print(f"Insertionsort n: {size} tiempo: {finalInsertion-inicioInsertion}")

        inicioMerge =time.time()
        mergesort.mergeSort(listaB,0,len(listaB)-1)
        finalMerge = time.time()
        print(f"mergesort_____n: {size} tiempo: {finalMerge-inicioMerge}")

        inicioBurbuja =time.time()
        Burbuja.burbuja(listaC)
        finalBurbuja = time.time()
        print(f"Ordenamiento_BURBUJA n: {size} tiempo: {finalBurbuja-inicioBurbuja}")

        inicioSeleccion =time.time()
        Seleccion.seleccion(listaF)
        finalSeleccion = time.time()
        print(f"Ordenamiento_seleccion n: {size} tiempo: {finalSeleccion-inicioSeleccion}")

        print("--------------------------------------------------------------------------------------------")
