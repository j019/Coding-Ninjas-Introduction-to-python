import sys

def intersections(arr1, n, arr2, m) :
    for i in range(0,len(arr1)):
        for j in range(0,len(arr2)):
            if arr1[i]== arr2[j]:
                arr2[j] = -1
                print(arr1[i],end=" ")
                break



#Taking Input Using Fast I/O
def takeInput() :
    n = int(input().strip())
    if n == 0:
        return list(), 0

    arr = [int(x) for x in input().split()]
    return arr, n


#main
t = int(input().strip())

while t > 0 :
    arr1, n = takeInput()
    arr2, m = takeInput()

    intersections(arr1, n, arr2, m)
    print()

    t -= 1