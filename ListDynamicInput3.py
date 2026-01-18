def summation(arr):
    sum = 0

    for i in range(len(arr)):
        sum = sum+arr[i]
    return sum

def main():
    size = 0
    value = 0
    ret = 0

    print("Please enter the size of number:")
    size = int(input())
    data = list()

    print("Enter the elements :")
    
    for i in range(size):
        value = int(input())
        data.append(value)
    
    ret = summation(data)
    
    print("Summation is :", ret)

if __name__ == "__main__":
    main()

