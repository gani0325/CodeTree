M, D = map(int, input().split())

# Please write your code here.
def date(M, D):
    odd = [1, 3, 5, 7, 8, 10, 12]
    even = [2, 4, 6, 9, 12]
    if M > 12 or D > 31:
        return "No"
    if M == 2 and D > 28:
        return "No"
    if D == 30:
        if M in even:
            return "Yes"
        else:
            return "No"
    elif D == 31:
        if M in odd:
            return "Yes"
        else:
            return "No"
    else:
        return "Yes"
print(date(M, D))