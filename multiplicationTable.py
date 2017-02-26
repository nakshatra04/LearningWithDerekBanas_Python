import math

def multiplicationTable(upto):
    numList = [[0] * 10 for i in range(int(upto))]

    i = 1
    j = 1
    for i in range(1,11):
        for j in range(1,len(numList)+1):
            numList[i-1][j-1] = i*j

    for i in range (len(numList)):
        print numList[i]



multiplicationTable(10)
