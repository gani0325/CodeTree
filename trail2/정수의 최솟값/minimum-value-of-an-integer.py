a, b, c = map(int, input().split())

# Please write your code here.
def _min(a, b, c):
    temp = min(a, b)
    _temp = min(temp, c)
    return _temp

print(_min(a, b, c))