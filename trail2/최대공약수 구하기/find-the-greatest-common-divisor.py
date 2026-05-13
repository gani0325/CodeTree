n, m = map(int, input().split())

# Please write your code here.
def gcd(n, m):
    while m:
        n, m = m, n % m
    return n

print(gcd(n, m))