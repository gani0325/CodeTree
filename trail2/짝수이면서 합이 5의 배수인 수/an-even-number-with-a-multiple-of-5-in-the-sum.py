n = int(input())

# Please write your code here.
def compare(n):
    total = n // 10 + n % 10
    if n % 2 == 0 and total % 5 == 0:
        return print("Yes")
    else:
        return print("No")

compare(n)