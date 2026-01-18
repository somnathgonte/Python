# Procedural 

def checkEven(No):         # Argument (No)
    return (No%2 == 0)
       

def main():
    value = 0
    ret = False

    print("Enter Number :")
    value = int(input())    # type conversion string to integer

    ret = checkEven(value)        # Parameter (value)
    if (ret == True) :
        print("It is Even")
    else :
        print("It is odd")
    
if __name__=="__main__":
    main()