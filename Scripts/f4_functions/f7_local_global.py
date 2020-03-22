x = 10 # global

def funct():
    x = 10
    x = x + 10 # local scope
    print("funct", x)
    
funct()
funct()
funct()
print(x)