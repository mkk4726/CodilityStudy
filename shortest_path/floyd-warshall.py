def floyd_warshall(n, graph):
    # 거리 행렬 초기화 (그래프 복사)
    dist = [[float('inf')] * n for _ in range(n)]

    # 자기 자신까지의 거리는 0으로 설정
    for i in range(n):
        dist[i][i] = 0

    # 초기 그래프 값 복사
    for u, v, w in graph:
        dist[u][v] = w  # 유향 그래프 (단방향)

    # 플로이드-워셜 알고리즘 수행
    for k in range(n):  # 경유지 k
        for i in range(n):  # 출발지 i
            for j in range(n):  # 도착지 j
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

# 테스트 (예제 그래프)
n = 4  # 노드 개수
graph = [
    (0, 1, 4),
    (0, 2, 1),
    (1, 3, 1),
    (2, 1, 2),
    (2, 3, 5),
    (3, 0, 7)
]

# 실행
result = floyd_warshall(n, graph)

# 결과 출력
for row in result:
    print(row)
