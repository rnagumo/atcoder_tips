
"""
問題: https://atcoder.jp/contests/abc130/tasks/abc130_e
解説: https://drken1215.hatenablog.com/entry/2019/06/21/230200

共通部分列を数え上げる問題．
"""


def main1():
    """LCS (Longest Common Sequence)を改良する．

    LCSでは最長部分列の長さを求めるが，今回は個数を求める．
    重複して数えている分を引けば良い．
    """

    N, M = map(int, input().split())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))

    dp = [[0] * (M + 1) for _ in range(N + 1)]
    MOD = 10 ** 9 + 7

    for i in range(N + 1):
        dp[i][0] = 1

    for j in range(M + 1):
        dp[0][j] = 1

    for i in range(N):
        for j in range(M):
            if S[i] == T[j]:
                dp[i + 1][j + 1] += dp[i][j]
            dp[i + 1][j + 1] += dp[i][j + 1] + dp[i + 1][j] - dp[i][j]
            dp[i + 1][j + 1] %= MOD

    print(dp[-1][-1])


def main2():
    """総和のための配列を別に用意する．"""

    N, M = map(int, input().split())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))

    dp = [[0] * (M + 1) for _ in range(N + 1)]
    sdp = [[0] * (M + 2) for _ in range(N + 2)]
    MOD = 10 ** 9 + 7

    dp[0][0] = 1
    sdp[1][1] = 1

    for i in range(N + 1):
        for j in range(M + 1):
            if i == 0 and j == 0:
                continue
            if i >= 1 and j >= 1 and S[i - 1] == T[j - 1]:
                dp[i][j] = sdp[i][j]
            sdp[i + 1][j + 1] = (sdp[i + 1][j] + sdp[i][j + 1] - sdp[i][j]
                                 + dp[i][j])
            sdp[i + 1][j + 1] %= MOD

    print(sdp[-1][-1])


if __name__ == "__main__":
    # main1()
    main2()
