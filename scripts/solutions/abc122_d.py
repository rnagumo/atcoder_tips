
"""
https://atcoder.jp/contests/abc122/tasks/abc122_d

以下の条件を満たす"AGCT"の文字列の数を求める．
* "AGC"を部分文字列として含まない
* 隣接する2文字を入れ替えて"AGC"にならない

隣接する4文字のみで可否が決まるので，メモ化再帰で計算できる．
* ok関数は，4文字を受け取って，隣同士の入れ替えでAGCを実現できるかを調べている．
* dfs関数は，3文字を受け取り後ろに1文字を足し，それが条件を満たす場合には次へ進む．
  初期値は"TTT"として判定に影響が出ないようにする．
"""

N = int(input())
MOD = 10 ** 9 + 7
memo = [{} for _ in range(N + 1)]


def ok(last4):
    for i in range(4):
        t = list(last4)
        if i >= 1:
            t[i - 1], t[i] = t[i], t[i - 1]

        if "".join(t).count("AGC") > 0:
            return False

    return True


def dfs(cur, last3):
    if last3 in memo[cur]:
        return memo[cur][last3]

    if cur == N:
        return 1

    ret = 0
    for c in "ACGT":
        if ok(last3 + c):
            ret = (ret + dfs(cur + 1, last3[1:] + c)) % MOD
    memo[cur][last3] = ret
    return ret


print(dfs(0, "TTT"))
