import random as random
a = random.randint(1,30)
print(a)
b = int(input("Enter number"))
if a == b:
    print("contagtulations!, your answer is correct")
else:
    if a>b:
        print("your answer is wrong, hidden number is greater than the entered number")
        c = int(input("enter another number"))
        if c == a:
            print("contagtulations!, your answer is correct")
        else:
            if c>a:
                print("your answer is wrong, hidden number is less than the entered number")
                d = int(input("enter number: "))
                if d == a:
                    print("contagtulations!, your answer is correct")
                else:
                    if d>a:
                        print("your answer is wrong, hidden number is less than the entered number")
                    
                    elif d<a:
                        print("your answer is wrong, hidden number is greater than the entered number")
            elif c<a:
                print("your answer is wrong, hidden number is greater than the entered number")
                d = int(input("enter number: "))
                if d == a:
                    print("contagtulations!, your answer is correct")
                else:
                    if d>a:
                        print("your answer is wrong, hidden number is less than the entered number")
                    
                    elif d<a:
                        print("your answer is wrong, hidden number is greater than the entered number")
        
    elif a<b:
        print("your answer is wrong, hidden number is less than the entered number")
        c = int(input("enter another number"))
        if c == a:
            print("contagtulations!, your answer is correct")
        else:
            if c>a:
                print("your answer is wrong, hidden number is less than the entered number")
                d = int(input("enter number: "))
                if d == a:
                    print("contagtulations!, your answer is correct")
                else:
                    if d>a:
                        print("your answer is wrong, hidden number is less than the entered number")
                    
                    elif d<a:
                        print("your answer is wrong, hidden number is greater than the entered number")
            elif c<a:
                print("your answer is wrong, hidden number is greater than the entered number")
                d = int(input("enter number: "))
                if d == a:
                    print("contagtulations!, your answer is correct")
                else:
                    if d>a:
                        print("your answer is wrong, hidden number is less than the entered number")
                    
                    elif d<a:
                        print("your answer is wrong, hidden number is greater than the entered number")