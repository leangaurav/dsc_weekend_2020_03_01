x = 10 # global

def funct():
    global x
    x = x + 10 # local scope
    print("funct", x)
    
funct()
funct()
funct()
print(x)