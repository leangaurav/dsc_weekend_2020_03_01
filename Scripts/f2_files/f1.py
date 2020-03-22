f = open('test.txt', 'w')
print("Something", file = f)
print("This is next line", 4242, 5, file = f)
f.close()