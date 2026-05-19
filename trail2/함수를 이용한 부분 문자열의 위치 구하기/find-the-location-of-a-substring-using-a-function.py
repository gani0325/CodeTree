text = input()
pattern = input()

# Please write your code here.
def solution(text, pattern):
    result = -1
    for i in range(len(text) - len(pattern) + 1):
        if text[i:len(pattern)+i] == pattern:
            return i
    return result

print(solution(text,pattern))