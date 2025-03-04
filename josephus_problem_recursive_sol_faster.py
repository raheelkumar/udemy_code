def findTheWinner(n,k):
    def joseph(n):
        if n==1:
            return 0
        return (joseph(n-1)+k)%n
    return joseph(n)+1

print(findTheWinner(5,2))