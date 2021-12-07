## Read input as specified in the question
## Print the required output in given format
n = int(input())
for i in range(n, 0, -1):
    for j in range(0, i):
        print(i, end="")
    print()