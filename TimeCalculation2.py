import time 

def factorial(No):
    fact = 1
    
    for i in range(1, No+1):
        fact = fact * i
    
    return fact

def main():
    value = int(input("Enter Number :"))

    start_time = time.time()

    ret = factorial(value)

    end_time = time.time()

    print("Factorial is :",ret)
    print("Total Execution time is :",end_time-start_time)
    
if __name__ == "__main__":
    main()