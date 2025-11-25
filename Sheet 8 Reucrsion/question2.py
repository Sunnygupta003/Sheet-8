def unique(arr):
    d=0
    for i in arr:
        d ^=i
    return d
arr = [2, 3, 4, 5, 4, 3, 2]
print("The unquie element is:", unique(arr))