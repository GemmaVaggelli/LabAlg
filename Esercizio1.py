import numpy as np
import time 
def insertionsort(A):       
    for j in range(1,len(A)):
        key = A[j]
        i = j-1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
def merge(A, l, m, r): 
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1) 
    R = [0] * (n2) 
    for i in range(0 , n1): 
        L[i] = A[l + i] 
    for j in range(0 , n2): 
        R[j] = A[m + 1 + j] 
    i = 0     
    j = 0     
    k = l  
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            A[k] = L[i] 
            i += 1
        else: 
            A[k] = R[j] 
            j += 1
        k += 1
    while i < n1: 
        A[k] = L[i] 
        i = i + 1
        k += 1
    while j < n2: 
        A[k] = R[j] 
        j += 1
        k += 1        
def mergesort(A, l, r):
    if l < r :
        m= (l+(r-1))/2
        m=int(m)
        mergesort(A, l, m) 
        mergesort(A, m+1, r)
        merge(A, l, m, r)

def BGenerator(j,lenght):
    if j=="random":
        return np.random.randint(1,lenght,lenght)
    if j=="sorted":
        return np.arange(lenght)
    if j=="reversed":
        return np.arange(lenght,-1,-1)

C=np.arange(0, 1000000 ,200)
for j in ["random","sorted","reversed"] :
    totalTimer=120
    i=0
    lastLoop=0   
    file=open("output- " + j + ".csv", "w")
    while totalTimer >= lastLoop :
        globalstart = time.time()
        B=BGenerator(j,C[i])
        A=B.copy()
        start = time.time()
        mergesort(B,0,C[i]-1)
        end1 = time.time()
        insertionsort(A)
        end2 = time.time()
        file.write("%s,%.0f,%.0f\n" % (C[i] , (end1 - start)*1000,(end2 - end1)*1000))
        # print("MergeSort- ["+ str(C[i]) +"]: " + str(end1 - start))
        # print("InsertionSort - [" + str(C[i]) +"]: " + str(end2 - start))
        i=i+1
        globalend = time.time()
        lastLoop=(globalend - globalstart)
        totalTimer= totalTimer - lastLoop
    file.close()
            


