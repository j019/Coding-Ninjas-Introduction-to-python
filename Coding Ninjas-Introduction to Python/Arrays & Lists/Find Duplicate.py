import sys

def duplicateNumber(arr, n) :
        count=0
        if (n==2):
                return (0)
        else :
             for i in range(0,len(arr)):
                for j in range(i+1,len(arr)):
                    if arr[i]==0:
                        continue
                    elif arr[i]== arr[j]:
                        count= count +1 
                        return arr[i]
                        break
                



#Taking Input Using Fast I/O
def takeInput() :
    n = int(input().strip())

    if n == 0 :
        return list(), 0

    arr = [int(x) for x in input().split()]
    return arr, n


#main
t = int(input().strip())

while t > 0 :
    
    arr, n = takeInput()
    print(duplicateNumber(arr, n))

    t -= 1