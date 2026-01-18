def main():
    size = 0
    value = 0

    print("Please enter the number of elements :")
    size = int(input())
    data = list()

    for i in range(size):
        value = int(input())
        data.append(value)
    
    print(data)

if __name__ == "__main__":
    main()

