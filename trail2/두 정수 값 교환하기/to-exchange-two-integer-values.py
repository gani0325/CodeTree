n, m = map(int, input().split())

# Please write your code here.
def swap(n, m):
    temp = n
    n = m
    m = temp
    return n, m

a, b = swap(n, m)
print(a, b)