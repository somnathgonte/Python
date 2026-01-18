
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

def reduceX(task, elements):
    sum = 0
    # [11, 21, 23, 31]
    for no in elements:
        sum = task(sum,no)
    
    return sum
