## Read input as specified in the question
## Print the required output in given format
n = int(input())
i=0
j=0
while(i<n):
    j=0
    k=0
    original= ord('A') + i
    while(j<=i):
        target= original +k
        print(chr(target),end="")
        j= j + 1
        k= k+1
    i= i+1
    print()