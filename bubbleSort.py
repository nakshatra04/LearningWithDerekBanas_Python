import random

#Selection Sort

def selectionSort(arr):

    n = len(arr)
    for i in range(n):
        min_indx = i
        for j in range (i, n):
            if (arr[j] < arr[min_indx]):
                min_indx = j

        arr[i] , arr [min_indx] =  arr[min_indx], arr[i]
    print "After Selection Sort \n", arr


numList1 = []
for i in range(10):
    numList1.append(random.randrange(1, 100))

print "Before sorting \n", numList1
selectionSort(numList1)

#Bubble Sort

def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range (n-i-1):
            if (arr[j+1] < arr [j]):
                arr [j+1] , arr [j] = arr[j], arr[j+1]

    print "After Bubble Sort \n", arr

numList2 = []
for i in range(10):
    numList2.append(random.randrange(1, 100))

print "Before sorting \n", numList2
bubbleSort(numList2)

#Insertion Sort

def insertionSort(arr):
    n = len(arr)

    for i in range (1,n):
        key = arr[i]
        j = i-1
        while (j>=0 and arr[j]>key):
            arr [j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    print "After insertion Sort \n", arr

numList3 = []
for i in range(10):
    numList3.append(random.randrange(1, 100))

print "Before sorting \n", numList3

insertionSort(numList3)

#Merge Sort

def merge(arr, l, m,r):

    n1 = m-l+1
    n2 = r-m
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range (0,n1):
        L[i] = arr[l+i]
    for j in range (0,n2):
        R[j] = arr[m+j+1]

    i=0
    j=0
    k=l
    while (i<n1 and n2>j):
        if L[i]<= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k+=1

    while (i<n1):
        arr[k] = L[i]
        k +=1
        i+=1

    while (j<n2):
        arr[k] = R[j]
        k +=1
        j+=1




def mergeSort(arr,l,r):
    if (l<r):

        m = (l+(r-1))/2
        mergeSort(arr,l,m)
        mergeSort(arr,m+1,r)
        merge (arr,l,m,r)



numList4 = []
for i in range(10):
    numList4.append(random.randrange(1, 100))

print "Before sorting \n", numList4

l= 0
r= len(numList4)
mergeSort (numList4,l,r-1)
print "After Merge sort \n", numList4





