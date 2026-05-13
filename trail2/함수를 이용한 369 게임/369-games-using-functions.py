a, b = map(int, input().split())

# Please write your code here.
def check(a, b):
    total = 0
    
    for i in range(a, b+1):
        if any(d in str(i) for d in "369") or i % 3 == 0 :
            total += 1
    return total

print(check(a, b))