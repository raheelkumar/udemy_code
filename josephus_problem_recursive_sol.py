def findTheWinner(array, start):
    if len(array)==1:
        # print('final_array: ',array)
        return array[0]
    rm = (start+k-1)%(len(array))
    # print('removed pos: ',rm)
    array.pop(rm)
    # print('array: ',array)
    return findTheWinner(array,rm)


n = int(input("Enter group size: "))
k = int(input("Enter skip size: "))
array = [1] * n
for j in range(1, n+1):
    array[j-1] = j
# print('init_array: ',array)
print('winner is:',findTheWinner(array,0))

