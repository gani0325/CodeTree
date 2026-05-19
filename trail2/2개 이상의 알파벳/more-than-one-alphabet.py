A = input()

# Please write your code here.
def solution(A):
    if len(set(A)) < 2:
        return "No"
    else:
        return "Yes"

print(solution(A))