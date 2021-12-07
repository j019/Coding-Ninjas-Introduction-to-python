from sys import stdin
def isPermutation(string1, string2) :
        string3= ""
        if (len(string1)== len(string2)):
            a = sorted(string1)
            string1 = "".join(a)
            b = sorted(string2)
            string2 = "".join(b)
            if (string1== string2):
                return True
            else:
                return False
        else:
            return False


#main
string1 = input().strip();
string2 = input().strip();

ans = isPermutation(string1, string2)

if ans :
    print('true')
else :
    print('false')