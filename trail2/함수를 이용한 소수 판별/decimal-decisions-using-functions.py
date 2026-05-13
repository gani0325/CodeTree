a, b = map(int, input().split())

# Please write your code here.
def _prime(a, b):
    result = 0
    for i in range(a, b+1):
        if i < 2:
            continue
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            result += i
    return result

print(_prime(a, b))