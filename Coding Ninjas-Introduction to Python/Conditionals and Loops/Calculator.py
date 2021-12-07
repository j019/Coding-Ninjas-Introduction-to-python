# Write your code here
while True:
    choice = int(input())
    if choice>=1 and choice<=6:
        if choice == 1:
            num1 = int(input())
            num2 = int(input())
            res = num1 + num2
            print(res)
        elif choice == 2:
            num1 = int(input())
            num2 = int(input())            
            res = num1 - num2
            print(res)
        elif choice == 3:
            num1 = int(input())
            num2 = int(input())
            res = num1 * num2
            print(res)
        elif choice == 4:
            num1 = int(input())
            num2 = int(input())            
            res = num1 // num2
            print(res)
        elif choice == 5:
            num1 = int(input())
            num2 = int(input())
            res = num1 % num2
            print(res)
        elif choice == 6:
            exit()
    else:
        print("Invalid Operation")

