from collections import defaultdict


def func(X, Y):
    a, b, c = X
    p, q, r = Y
    return abs(p - a) + abs(q - b) + max(0, r - c)


def main():
    N = int(input())
    X = [list(map(int, input().split())) for _ in range(N)]

    graph = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            graph[i][j] = func(X[i], X[j])

    all_sets = defaultdict(list)
    for n in range(2 ** N):
        all_sets[bin(n).count("1")].append(n)

    dist = [[0] * N for _ in range(2 ** N)]
    for k in range(1, N):
        dist[1 << k][k] = graph[0][k]

    for s in range(2, N):
        for bit in all_sets[s]:
            for k in range(N):
                if bit >> k & 1 == 0:
                    continue

                bit_rm = bit - 2 ** k
                dist[bit][k] = min(
                    dist[bit_rm][m] + graph[m][k] for m in range(N) if bit_rm >> m & 1
                )

    print(min(dist[2 ** N - 2][k] + graph[k][0] for k in range(1, N)))


if __name__ == "__main__":
    main()
