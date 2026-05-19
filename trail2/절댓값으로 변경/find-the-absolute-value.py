n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def solution(n, arr):
    temp = []
    for i in range(n):
        temp.append(abs(arr[i]))
    return temp

result = solution(n, arr)
for i in range(n):
    print(result[i], end= " ")