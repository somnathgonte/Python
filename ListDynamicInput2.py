def main():
    size = 0
    value = 0

    print("Please enter the size of number:")
    size = int(input())
    data = list()

    print("Enter the elements :")
    
    for i in range(size):
        value = int(input())
        data.append(value)
    
    sum = 0

    for i in range(size):
        sum = sum+data[i]
    
    print("Summation is :", sum)


if __name__ == "__main__":
    main()

