def num(n):
    if n==0:
        return 1  
    else:
         num(n-1)
         return print(n)
    
    
n=int(input(" "))
print(num(n))