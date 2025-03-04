'''Coding Exercise: Josephus problem
There are n friends that are playing a game. The friends are sitting in a circle and are numbered from 1 to n in clockwise order. 
More formally, moving clockwise from the ith friend brings you to the (i+1)th friend for 1 <= i < n, and moving clockwise from the nth friend brings you to the 1st friend. 
The rules of the game are as follows: Start at the 1st friend. Count the next k friends in the clockwise direction including the friend you started at. 
The counting wraps around the circle and may count some friends more than once. The last friend you counted leaves the circle and loses the game. 
If there is still more than one friend in the circle, go back to step 2 starting from the friend immediately clockwise of the friend who just lost and repeat. 
Else, the last friend in the circle wins the game. Given the number of friends, n, and an integer k, return the winner of the game.'''

def findTheWinner(n, k):
    # write code here
    array = [1] * n

    for j in range(1, n+1):
        array[j-1] = j
    count = n


    # print()
    # print('count: ',count)
    itr = 0
    i=0
    while(count>1):
        if i == n:
            i = 0
        if count <= 1:
            break
        # print()
        # print('i: ', i)
        # print('itr: ',itr)
        # print('array: ', array)
        # print('array[',i,']: ',array[i])
        if array[i] != 0:
            itr += 1
            # print('itr++')
            if itr == k:
                # print('\nmatched_itr: ',itr)
                array[i] = 0
                # print('updated_array: ', array)
                count -= 1
                # print('updated_count: ',count)
                itr = 0
        i+=1



    for i in range(n):
        if array[i] != 0:
            return array[i]

n = int(input("Enter group size: "))
k = int(input("Enter skip size: "))
print('winner is:',findTheWinner(n,k))