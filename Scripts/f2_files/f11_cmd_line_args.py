import sys

print(sys.argv)

with open(sys.argv[0] ,'r') as f1:
    file_name  = '-copy.'.join(sys.argv[0].split('.'))
    with open(file_name, 'w') as f2:
        f2.write(f1.read())