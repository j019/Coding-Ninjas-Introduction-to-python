import sys

def findSingle( ar, n):
     
    res = ar[0]
     
    # Do XOR of all elements and return
    for i in range(1,n):
        res = res ^ ar[i]
     
    return res
 
#Taking Input Using Fast I/O
def takeInput() :
    n = int(sys.stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    return arr, n


#main
t = int(sys.stdin.readline().rstrip())

while t > 0 :

    arr, n = takeInput()
    print(findSingle(arr, n))

    t -= 1