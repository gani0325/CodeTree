n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def solution(n, arr):
    for i in range(n):
        if arr[i] % 2 == 0:
            arr[i] = int(arr[i] / 2)
    return arr

temp = solution(n, arr)
for i in range(n):
    print(temp[i], end=" ")