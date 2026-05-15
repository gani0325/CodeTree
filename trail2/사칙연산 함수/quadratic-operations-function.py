a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
def function(a, o, c):
    temp = 0

    if o == '+':
        temp = a + c
        return temp
    elif o == "-":
        temp = a - c
        return temp
    elif o == "/":
        temp = a / c
        return int(temp)
    elif o == "*":
        temp = a * c
        return temp
    else:
        return False

result = function(a, o, c)
if result is False:
    print(result)
else:
    print(f"{a} {o} {c} = {result}")