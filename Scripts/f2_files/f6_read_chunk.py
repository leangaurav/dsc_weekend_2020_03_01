with open('numbers1.txt', 'r') as f:

    content = f.read(5)
    while content:
        print(content, end='')
        content = f.read(5) 
        print("Pointer:", f.tell())