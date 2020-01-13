def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
a=60
b=48
print(gcd(a,b)) #12

#method2
def gcd(x, y):
    while (y):
        x, y = y, x % y

    return x 
print(gcd(x,y))
