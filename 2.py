def sumNum(a,b):
    if b == 0:
        return a
    else:
        return sumNum(b, a % b)
a = 12
b = 20
result = sumNum(a,b)   
print(result)

