# Read input as sepcified in the question
# Print output as specified in the question

S = int(input())
E = int(input())
W = int(input())
while S<=E:
    F=S
    C = ((F-32))*(5/9)
    print(S,end=" ")
    print(int(C))
    S=S+W