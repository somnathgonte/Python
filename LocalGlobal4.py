no = 11         # Global Variable

def fun():
    global no
    print("Value of No from fun is :", no) #11
    no = no + 1
    print("Value of No from fun is :", no) #12
   
print("Value of No is :", no)
fun()
print("Value of No is :", no)
