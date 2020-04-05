try:
    n = int(input())
    i = 10//n
    print(i)
    a = [1,2,3,4,5,6]
    print(a[i])
except ValueError as err:
    print("ValueError", err)
except ZeroDivisionError:
    print("ZeroDivisionError")
except:
    print("Something went wrong!!")

print("After Exception")
