def is_num(r):
    if r%2==0:
        print("Even number")
    else:
        print("Odd number")

n=int(input("Enter the number:-"))
is_num(n)

def is_num(r):
    if r%2==0:
        return "Even number"
    else:
        return "Odd number"

n=int(input("Enter the number:-"))
print(is_num(n))

