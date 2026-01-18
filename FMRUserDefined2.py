from functools import reduce

checkEven =lambda No : (No%2==0)
increment = lambda No : No+1
add = lambda a,b: a+b

def filterX(task, elements):
    result = list()

    for no in elements:
        ret = task(no)

        if (ret==True):
            result.append(no)

    return result 

def mapX(task, elements):
    result = list()

    for no in elements:
        ret = task(no)
        result.append(ret)
    return result



def main():
    Data = [11,10,15,20,22,27,30]
    print("Actual data is :", Data)

    Fdata = list(filterX(checkEven, Data))
    print("Data After filter is :", Fdata)

    Mdata = list(mapX(increment, Fdata))
    print("Data After Map is :", Mdata)

    Rdata = reduce(add, Mdata)
    print("Data after reduce is :", Rdata)

if __name__ == "__main__":
    main()