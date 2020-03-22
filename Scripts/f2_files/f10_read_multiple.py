with open('numbers1.txt', 'r') as f:
    print("Read1", repr(f.read()))
    print("Read2", repr(f.read()))
    f.seek(10)
    print("Read2", repr(f.read()))
  