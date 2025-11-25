n=int(input(" "))
a=list(map(int,input().split()))

for i in a:
    if i == i[::-1]:
        print(i , " number is palindrom")
    else:
        print(i)