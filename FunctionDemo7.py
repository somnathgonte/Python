# Accept : Multiple Parameters
# Return : One Value
def marvellous1(value1, value2):
    print("Inside Marvellous1 :", value1, value2)
    return 11

def main():
    result = None
    result = marvellous1("Python", 21)
    print("Return Value is : ", result)

if __name__=="__main__":
    main()