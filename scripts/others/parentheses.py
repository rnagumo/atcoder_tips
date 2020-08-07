
"""
https://www.geeksforgeeks.org/check-for-balanced-parentheses-in-an-expression/

Check for balanced parentheses in an expression

in: [()]{}{[()()]()}
out: Balanced

in: [(])
out: Not Balanced

---
stackを使って，順序通りに出ているかを調べる．最後にstackが空になっているかも確認する．
time: O(N), space: O(N)
"""

S = input()
stack = []
ok = True
for v in S:
    if v in "[{(":
        stack.append(v)
    else:
        last = stack.pop()
        if ((last == "{" and v == "}") or (last == "(" and v == ")")
                or (last == "[" and v == "]")):
            continue
        else:
            ok = False

if ok and not stack:
    print("Balanced")
else:
    print("Not Balanced")
