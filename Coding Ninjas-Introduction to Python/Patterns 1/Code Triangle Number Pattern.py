## Read input as specified in the question
## Print the required output in given format
rows = int(input())  
# Outer loop will print number of rows  
for i in range(rows+1):  
    # Inner loop will print the value of i after each iteration  
    for j in range(i):  
        print(i, end="")  # print number  
    # line after each row to display pattern correctly  
    print(" ")  