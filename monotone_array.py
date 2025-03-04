def monotonic_array(array):
    #write code here
    n = len(array)
    monotinic = True
    if n == 0:
        return monotinic
    
    first = array[0]
    last = array[n-1]

    if first > last:
        for j in range(n-1):
            if array[j] < array[j+1]:
                monotinic = False
    elif first == last:
        for j in range(n-1):
            if array[j] != array[j+1]:
                monotinic = False
    else:
        for j in range(n-1):
            if array[j] > array[j+1]:
                monotinic = False
    return monotinic


array = [1.2,3,4,5,6,5]
#array = [2,2,2,2,1,2]
result = monotonic_array(array)
print(result)