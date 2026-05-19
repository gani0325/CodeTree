A = input()

# Please write your code here.
def solution(A):
    temp = []
    for i in range(len(A)-1, -1, -1):
        temp.append(A[i])
    temp = "".join(temp)
    
    if temp == A:
        return "Yes"
    else:
        return "No"

print(solution(A))