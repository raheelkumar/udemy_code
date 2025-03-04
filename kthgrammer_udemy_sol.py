def kth_symbol(n, k):
    if n == 1:
        return 0

    mid = (2**(n-1))//2
    if k <= mid:
        return (kth_symbol(n-1, k))
    else:
        return int(not(kth_symbol(n - 1, k-mid)))

print(kth_symbol(3,4))