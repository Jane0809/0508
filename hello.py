def swap(a, idx1, idx2)
    a[idx1]=a[idx1] ^ a[idx2]
    a[idx2]=a[idx2] ^ a[idx1]
    a[idx1]=a[idx1] ^ a[idx2]
a = [1,2,3,4,5,6]
swap
print(a)