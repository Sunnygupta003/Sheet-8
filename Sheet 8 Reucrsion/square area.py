def sqr(n,power=2):
    if power==0:
        return 1 
    else:
        return n*sqr(n,power-1)
    

n=int(input(" "))
print(sqr(n))