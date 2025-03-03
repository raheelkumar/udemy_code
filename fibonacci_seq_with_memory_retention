def nth_fibonacco_num(memo, n):
    if n <= 1:
        return n

    if memo[n] != -1:
        return memo[n]

    memo[n] = nth_fibonacco_num(memo, n-1) + nth_fibonacco_num(memo, n-2)

    return memo[n]

def fib(n):
    memo = [-1] * (n+1)

    return nth_fibonacco_num(memo, n)

if __name__ == "__main__":
    n = 7
    for i in range(n):
        print(fib(i))