
x = 10 # global
def funct():
    x = 100 # local scope
    print("funct", x)

funct()
print(x)