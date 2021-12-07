## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())

ones = True

while n > 0:

  out = ["1"]*n if ones else ["0"]*n

  ones = not ones

  n -= 1

  print("".join(out))