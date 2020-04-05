def funct(x):
    if x == 0:
        raise ValueError("I raised")
    else:
        print("All is well!!!")
        
        
try:

    funct(0)
except Exception as err:
    print(err)
    
print("End")