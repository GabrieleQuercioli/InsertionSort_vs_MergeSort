import math
from timeit import default_timer as timer
import numpy as np
import matplotlib.pyplot as plt


def testAlgorithms(typeVector):
    timeInsertion = []
    timeMergesort = []
    avgInsertion = []
    avgMerge = []
    d = []
    dim = 10
    for j in range(1, 50):                                 # da 10 a 10^4=10000
        d.append(dim)
        if typeVector == 'RandomCase':
            A = randomize(dim)                       # ** operatore esponenziale
        if typeVector == 'OrderedCase':
            A = orderedVec(dim)
        if typeVector == 'OrderedDecCase':
            A = reversedVec(dim)

        for i in range(0, 3):                          # ripete ordinamento 3 volte su stesso array
            temp = []
            temp2 = []
            temp.extend(A)                                  # copio in array temp perchè senno nel merge parte con A già ordinato in insertion
            temp2.extend(A)                                 # extend per copiare per valore, non modificando A
            # print("temp: ", temp)
            timeInsertion.append(insertionSort(temp))
            # print("temp2: ", temp2)
            timeMergesort.append(timerMergeSort(temp2, 0, len(temp2) - 1))
        print("time insertion: ", timeInsertion)
        print("time merge: ", timeMergesort)
        totTimeInsertion = 0
        totTimeMerge = 0
        for i in range(0, len(timeInsertion)):
            totTimeInsertion += timeInsertion[i]
            totTimeMerge += timeMergesort[i]
        avgTimeI = totTimeInsertion / len(timeInsertion)
        avgTimeM = totTimeMerge / len(timeMergesort)
        avgInsertion.append(avgTimeI)
        avgMerge.append(avgTimeM)
        print("time tot insertion: ", totTimeInsertion)
        print("time tot merge: ", totTimeMerge)
        print("avg insertion: ", avgInsertion)
        print("avg merge: ", avgMerge)
        dim += 50                                                           # ogni volta il vettore ha 50 elementi in più
    plt.plot(d, avgInsertion, label="InsertionSort")
    plt.plot(d, avgMerge, label="MergeSort")
    plt.legend()
    plt.ylabel('Secondi')
    plt.xlabel('Ordinamento con vettore ' + typeVector)
    plt.show()


def randomize(dim):
    A = np.random.randint(0, dim*10, dim)                   # può scegliere numeri tra 0 e dim*10
    print("random: ", A)
    return A


def orderedVec(dim):
    A = np.random.randint(0, dim*10, dim)
    A = sorted(A)
    print("ordered: ", A)
    return A


def reversedVec(dim):
    A = np.random.randint(0, dim*10, dim)
    A = sorted(A, reverse=True)
    print("ordered dec", A)
    return A


def insertionSort(A):
    timelimit = 200            # FIXME si deve fermare dopo più tempo (è in secondi)
    startTimer = timer()
    for j in range(1, len(A)):  # parte dal secondo elemento (il sottoarray del primo è ordinato)
        # print(A)
        if timer()-startTimer > timelimit:              # FIXME
            print("sorting requested too much time")
            time = timelimit
            return float(time)
        else:
            key = A[j]  # salva l'elemento corrente
            i = j - 1  # i è l'ultimo elemento del sottovettore (già ordinato) prima di A[j]
            while i >= 0 and A[i] > key:  # confronta l'elemento in input con uno precedente A[i]
                A[i + 1] = A[i]  # shifta a dx l'elemento trovato > di key
                i = i - 1  # continua a scorrere l'indice del sottoarray ordinato
            A[i + 1] = key  # copia l'elemento in input nella corretta posizione
    time = timer() - startTimer
    print("insertion sorted: ", A)
    return float(time)


def timerMergeSort(A, p, r):
    startTimer = timer()
    mergeSort(A, p, r)
    time = timer() - startTimer
    print("merge sorted: ", A)
    return float(time)


def mergeSort(A, p, r):
    if p < r:
        q = (p + r) // 2  # parte intera inferiore
        # print(q)
        mergeSort(A, p, q)
        mergeSort(A, q + 1, r)
        merge(A, p, q, r)


def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):                  # copia la prima metà del vettore
        L[i] = A[p + i]
    for j in range(0, n2):                  # copia la seconda metà del vettore
        R[j] = A[q + j + 1]
    L.append(math.inf)
    R.append(math.inf)
    i = j = 0
    for k in range(p, r + 1):               # confronta a due a due i valori e mette in A il più piccolo
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1


if __name__ == '__main__':
    testAlgorithms('OrderedDecCase')
