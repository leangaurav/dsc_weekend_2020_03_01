def funct():
    try:
        n = int(input("INput :"))
        if i != 0:
            i = 10//n
          
            print(i)
            a = [1,2,3,4,5,6]
            d = {2:10}
            print(a[i])
            print(d[i])
        else:
            print("Please do not give 0.")
    except ValueError as err:
        print("Function1 ValueError", err)
    print("Function1 Success")
    
def funct2():
    try:
        funct()        
    except ZeroDivisionError:
        print("Function 2ZeroDivisionError")
    print("Function2 success")
        
try:
    funct2()
except KeyError:
    print("KeyError")
print("After Exception")
