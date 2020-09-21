
"""
https://atcoder.jp/contests/abc166/tasks/abc166_f

[A, B, C]から，クエリで指定された2文字のうち，一方は+1, 他方は-1する．常に全ての値が非負に
なるように処理する手順を求める．

基本的には，二文字のうち大きい方から引き，小さい方に足せばよい．問題は，両者が等しい時．
この時には，次のクエリに含まれる文字に足し，含まれない（かもしれない）方から引く．つまり，
確実に次のクエリで現れる文字に対してバッファを与えるイメージである．
"""

N, A, B, C = map(int, input().split())
S = [input() for _ in range(N)]

x = [A, B, C]
d = {"A": 0, "B": 1, "C": 2}
if sum(x) == 0:
    print("No")
else:
    flag = True
    ans = []
    for i, s in enumerate(S):
        n, m = list(s)

        if x[d[n]] == x[d[m]] == 0:
            flag = False
            break

        if x[d[n]] > x[d[m]]:
            x[d[n]] -= 1
            x[d[m]] += 1
            ans.append(m)
        elif x[d[n]] < x[d[m]]:
            x[d[n]] += 1
            x[d[m]] -= 1
            ans.append(n)
        elif i < N - 1 and S[i] != S[i + 1]:
            # x[d[n]] == x[d[m]]
            if n in S[i + 1]:
                x[d[n]] += 1
                x[d[m]] -= 1
                ans.append(n)
            else:
                x[d[m]] += 1
                x[d[n]] -= 1
                ans.append(m)
        else:
            # x[d[n]] == x[d[m]] at last
            x[d[n]] += 1
            x[d[m]] -= 1
            ans.append(n)

    if flag:
        print("Yes")
        print(*ans, sep="\n")
    else:
        print("No")
