## Note : For printing multiple values in one line, put them inside print separated by space.
## You can follow this syntax for printing values of two variables val1 and val2 separaetd by space -
## print(val1, " ", val2)
N = input()

total = 0
evens = 0

for c in N:
    c = int(c)
    total += c
    if c % 2 == 0:
        evens += c

odds = total - evens

print(evens, odds)