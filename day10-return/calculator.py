def count(num1,num2,operator):
    if(operator=="+"):
        print(f"{num1}+{num2}={num1+num2}")
        return num1+num2
    elif(operator=="-"):
        return num1-num2
    elif(operator=="-"):
        return num1-num2
    elif(operator=="-"):
        return num1-num2
    else:
        print("operator not found")
        return 
logo=logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
while(True):
    num1=float(input("whats the first number?:"))
    print("+\n-\n*\n/\n")
    operator=input("pick an opertor")
    num2=float(input("whats the next number?:"))
    num1=(count(num1,num2,operator))
    pilihan=input(f"type 'y' to continue calculating with {num1} or type 'n' to start a new calculation or type 'q' to quit  :")
    if(pilihan=='q'):
        break
    while(pilihan=='y'):
        operator=input("pick an opertor")
        num2=float(input("whats the next number?:"))
        num1=(count(num1,num2,operator))
        pilihan=input(f"type 'y' to continue calculating with {num1} or type 'n' to start a new calculation :")

    
    

        
        

