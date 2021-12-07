## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
i=n
while i>=1:
    j=i
    while j<=n:
        print(chr(ord('A') + j - 1), end ="")
        j=j+1
    i=i-1
    print()