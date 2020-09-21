
"""
https://atcoder.jp/contests/abc117/tasks/abc117_c

M個の地点{X}を，N個のコマで訪れるときの最小移動数を求める．

他と離れている地点にはコマを直接置いて，そこから動かさない．
他と近くにある地点には，他の地点からコマを動かして訪れる．
よって，ソートされた地点間の距離を求め，小さい方からM-N個を訪れれば良い．
"""

N, M = map(int, input().split())
X = list(map(int, input().split()))

X.sort()
diff = sorted(X[i + 1] - X[i] for i in range(M - 1))
print(sum(diff[:max(0, M - N)]))
