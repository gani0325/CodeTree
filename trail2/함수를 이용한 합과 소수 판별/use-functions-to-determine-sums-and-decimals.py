a, b = map(int, input().split())

def prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True          # for문 밖으로

def even(m):
    return sum(int(d) for d in str(m)) % 2 == 0

result = 0
for i in range(a, b+1):
    if prime(i) and even(i):
        result += 1

print(result)