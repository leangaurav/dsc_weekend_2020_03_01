with open('numbers1.txt', 'r') as f:

    content = f.readline()
    while content:
        print(content)
        content = f.readline() 