
"""
https://atcoder.jp/contests/abc154/tasks/abc154_e

1 <= x <= Nであって，0でない数字がちょうどK個あるようなものの個数を求める．

典型的な桁DPの問題．
"""

N = input()
K = int(input())

# dp[i桁目][確定しているか][0の数]
# j: 0 = 確定していない, 1 = 確定している
dp = [[[0] * (K + 1) for _ in range(2)] for _ in range(len(N) + 1)]
dp[0][0][0] = 1
for i in range(len(N)):
    n = int(N[i])
    for j in range(2):
        for k in range(K + 1):
            # d: その桁の数
            # 小さいことが確定している場合には，0~9まで全ての数を考える
            # 確定していない場合には，N[i]より小さい数のみ
            for d in range((9 if j == 1 else n) + 1):
                # 0でない桁の数が条件よりも小さい
                if k + int(d != 0) <= K:
                    # d < N[i]では確定する
                    dp[i + 1][j | (d < n)][k + int(d != 0)] += dp[i][j][k]

# N自身が条件を満たすかを確認する
n_self = int(len(N) - N.count("0") == K)

# 答え
print(dp[-1][-1][-1] + n_self)
