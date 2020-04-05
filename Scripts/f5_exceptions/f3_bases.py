try:
    n = int(input("INput :"))
    i = 10//n
    print(i)
    a = [1,2,3,4,5,6]
    d = {2:10}
    print(a[i])
    print(d[i])
except ValueError as err:
    print("ValueError", err)
except ZeroDivisionError:
    print("ZeroDivisionError")
except KeyError:
    print("KeyError")
except LookupError:
    print("Some kind of lookup error")
except Exception as e:
    print("Something went wrong!!", e)

print("After Exception")
