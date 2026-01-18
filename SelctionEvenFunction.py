def checkEven(No):
    if No%2 == 0:
        print("It is even number")
    else :
        print("It is odd number")

def main():
    
    checkEven(21)               # Positional
    checkEven(No=22)            # Keyword

if __name__=="__main__":
    main()