from functools import reduce

def main():
    Data = [11,10,15,20,22,27,30]
    print("Actual data is :", Data)

    Fdata = list(filter((lambda No : (No%2==0)), Data))
    print("Data After filter is :", Fdata)

    Mdata = list(map((lambda No : No+1), Fdata))
    print("Data After Map is :", Mdata)

    Rdata = reduce((lambda a,b: a+b), Mdata)
    print("Data after reduce is :", Rdata)

if __name__ == "__main__":
    main()