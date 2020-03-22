with open('numbers.txt', 'w') as f:
    print(dir(f))
    print(f.closed)
    for i in range(1,21):
        print(i, file = f) # some work on file

print(f.closed)
