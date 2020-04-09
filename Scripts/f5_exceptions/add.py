import sys

arg = sys.argv
if len(arg) == 3:
    n1 = int(arg[1])
    n2 = int(arg[2])
    print(n1 + n2)
else:
    print("Invalid number of arguments. Expected 2, got ", len(arg)-1)

