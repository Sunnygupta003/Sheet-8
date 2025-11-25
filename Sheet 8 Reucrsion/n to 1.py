def num(n):
    if n==0:
        return 1
    else:
         print(n)
         num(n-1)
         return 
    
    
n=int(input(" "))
print(num(n))