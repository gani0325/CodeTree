n = int(input())

# Please write your code here.
def _sum(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

result = _sum(n) // 10
print(result)