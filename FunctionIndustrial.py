# Procedural 

def checkEven(No):         # Argument (No)
    if No%2 == 0:
        return True
    else :
        return False

def main():
    value = 0
    ret = False

    print("Enter Number :")
    value = int(input())    # type conversion string to integer

    ret = checkEven(value)        # Parameter (value)
    print(ret)
    
if __name__=="__main__":
    main()