text = input()
pattern = input()

# Please write your code here.
def solution(text, pattern):
    for i in range(len(text) - len(pattern) + 1):
        if text[i:len(pattern)+i] == pattern:
            return i
    return -1

print(solution(text,pattern))