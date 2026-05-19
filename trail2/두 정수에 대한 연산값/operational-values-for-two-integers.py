a, b = map(int, input().split())

# Please write your code here.

def solution(a, b):
    #max
    if a > b:
        a = a + 25
        b = b * 2
        return a, b
    else:
        a = a * 2
        b = b + 25
        return a, b

n, m = solution(a, b)
print(n, m)

