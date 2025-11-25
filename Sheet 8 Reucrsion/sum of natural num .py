def sum_num(n):
   if n==1:
      return 1
   else:
      return n + sum_num(n-1)
    

n=int(input(" "))
print(sum_num(n))

