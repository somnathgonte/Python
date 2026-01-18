# Procedural 

def checkEven(No):         # Argument (No)
    if No%2 == 0:
        print("It is even number")
    else :
        print("It is odd number")


value = 0

print("Enter Number :")
value = int(input())    # type conversion string to integer

checkEven(value)        # Parameter (value)
    
