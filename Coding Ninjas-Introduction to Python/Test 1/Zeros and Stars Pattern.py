## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
m=n+1
for i in range(1, m):
    for j in range(1, (2*m)):
        if(i == j or j == m or i == (2*m)-j):
           print("*", end="")
        else:
           print( "0", end="")
    print()