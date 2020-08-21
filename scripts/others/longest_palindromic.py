
"""
https://leetcode.com/problems/longest-palindromic-substring/

与えられた文字列の最長の回文を出力する．

各文字について，それ自身が真ん中になるような回文を生成する．
ただし，奇数長の場合には自身が真ん中であり，偶数長の場合には自身と次の文字が真ん中になる．
それぞれの場合を調べる必要がある点に注意する．
計算量はO(N^2)．
"""


def check(s: str, l: int, r: int) -> str:
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l + 1:r]


S = input()
res = ""
for i in range(len(S)):
    # Odd case
    tmp = check(S, i, i)
    if len(tmp) > len(res):
        res = tmp

    # Even case
    tmp = check(S, i, i + 1)
    if len(tmp) > len(res):
        res = tmp

print(res)
