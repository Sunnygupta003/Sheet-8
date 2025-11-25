def prod(n):
    if n==0:
        return 1
    else:
        return (n%10)*(n//10)
    
n=int(input(" "))
print(prod(n))