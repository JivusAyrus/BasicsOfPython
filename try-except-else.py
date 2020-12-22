a, b = 1,0

try:
    print(a/b)
except ZeroDivisionError:
    print("division by zero")
else:
    print("no exceptions raised")
finally:
    print("Run this always")
