a, b = map(int, input().split())

def is_oneon(n):
    if n % 2 == 0:          # 조건1: 2로 나누어 떨어짐
        return False
    if n % 10 == 5:         # 조건2: 일의 자리가 5
        return False
    if n % 3 == 0 and n % 9 != 0:  # 조건3: 3의 배수이면서 9의 배수는 아님
        return False
    return True

def all(a, b):
    result = 0
    for i in range(a, b+1):
        if is_oneon(i):
            result += 1
    return result

print(all(a, b))