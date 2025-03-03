def kth_symbol(n, k):
    #write your code here
    if n == 1:
        return 0
    
    parent = kth_symbol(n-1, -(k//-2))
    
    iskodd = k % 2 == 1
    if parent == 1:
        return 1 if iskodd else 0
    else:
        return 0 if iskodd else 1