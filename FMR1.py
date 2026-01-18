def checkEven(No):
    return(No%2==0)

def main():
    Data = [11,10,15,20,22,27,30]
    print("Actual data is :", Data)

    Fdata = list(filter(checkEven, Data))
    print("Data After filter is :", Fdata)

if __name__ == "__main__":
    main()