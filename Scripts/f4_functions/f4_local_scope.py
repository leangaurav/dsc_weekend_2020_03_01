# local scope

def funct():
    x = 100 # local variable
    print("funct", x)
    
funct()
print(x)