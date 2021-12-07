## Read input as specified in the question
## Print the required output in given format
rows = int(input())
for i in range(1, rows+1):
    for j in range(i, 0, -1):
        print(j, end="")
    print("")