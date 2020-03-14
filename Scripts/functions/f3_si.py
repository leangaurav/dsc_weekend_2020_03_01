def si(p, r, t):    
    simple_i=(p*t*r)/100    
    return simple_i

p = int(input("enter p")) 
t = int(input("enter t")) 
r = int(input("enter r"))
print(si(p,r,t))

print(si(1000,3,4))
