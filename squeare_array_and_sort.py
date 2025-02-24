def sorted_squared(array):
    #write code here.make sure to return desired array
    n = len(array)-1
    m = n
    sq_arr = [0]*len(array)
    i = 0
    while i <= n:
        if array[i] **2 < array[n] ** 2:
            sq_arr[m] = array[n]**2
            n = n-1
            m = m-1
        elif array[i] **2 > array[n] ** 2:
            sq_arr[m] = array[i]**2
            i = i+1
            m = m-1
        else:
            sq_arr[m] = array[i]**2
            break
    return sq_arr

array = [-10,-3,5,9,11,12]
result = sorted_squared(array)
print(result)