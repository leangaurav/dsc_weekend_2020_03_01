v1 = 10 # global
print(v1)

def funct():
    v1 = 20 # local variable to funct
    print(v1)

funct()
funct()

print(v1)

if True:
    v3 = 40
    
print(v3)

def funct1():
    v2 = 30 # local to function cannot be accessed outside function
    print(v2)
    
funct1()
print(v2)
