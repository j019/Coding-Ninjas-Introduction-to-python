## Read input as specified in the question.
## Print output as specified in the question.
def pypart(n):
     
    # outer loop to handle number of rows
    # n in this case
    for i in range(0, n):
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
         
            # printing stars
            print("1",end="")
      
        # ending line after each row
        print("\r")
 
# Driver Code
n = int(input())
pypart(n)