
def display(a,b,c,d):
    print(a,b,c,d)

def main():
   # display(10,20)   Not allowed - Less arguments
   # display(10,20,30,40,50)  Not allowed - Extra arguments
   display(10,20,30,40)  #Allowed

if __name__ == "__main__":
    main()