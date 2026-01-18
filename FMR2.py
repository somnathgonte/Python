def checkEven(No):
    return(No%2==0)

def increment(No):
    return No+1

def main():
    Data = [11,10,15,20,22,27,30]
    print("Actual data is :", Data)

    Fdata = list(filter(checkEven, Data))
    print("Data After filter is :", Fdata)

    Mdata = list(map(increment, Fdata))
    print("Data After Map is :", Mdata)

if __name__ == "__main__":
    main()