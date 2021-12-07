#Write Your Code Here
# Ask for enter the number from the use  
number = int(input())  
  
# Initiate value to null  
revs_number = 0  
  
# reverse the integer number using the while loop  
  
while (number > 0):
    remainder = number % 10  
    revs_number = (revs_number * 10) + remainder  
    number = number // 10  
  
# Display the result  
print(revs_number)  