Y, M, D = map(int, input().split())

odd = [1, 3, 5, 7, 8, 10, 12]
even = [2, 4, 6, 9, 11]

def is_leap(Y):
    if Y % 400 == 0:
        return True
    if Y % 100 == 0:
        return False
    if Y % 4 == 0:
        return True
    return False

def season(Y, M, D):
    # 날짜 유효성 체크
    if M in odd and D > 31:
        return -1
    if M in even and D > 30:
        return -1
    if M == 2:
        if is_leap(Y) and D > 29:
            return -1
        if not is_leap(Y) and D > 28:
            return -1

    # 계절 판단 (M 기준으로 수정)
    if 3 <= M <= 5:
        return "Spring"
    elif 6 <= M <= 8:
        return "Summer"
    elif 9 <= M <= 11:
        return "Fall"
    else:
        return "Winter"

print(season(Y, M, D))