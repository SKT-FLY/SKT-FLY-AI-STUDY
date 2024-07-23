string = list(input())

word = ""

while string:
    s = string.pop()
    if s == "(":
        m = string.pop()
        word = word * int(m)
    elif s == ")":
        continue
    else:
        word += s

print(len(word))
