
try:
    n = int(input("INput :"))
    10/n
except ValueError as e:
    print("Something went wrong", e)
else: # can be there only if there is alteast one except
    print("There when everything' good")
finally:
    print("I'm always there")
    
print("End !!")