def read_txt_lines(path: str) -> list:
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()  # 전체 줄을 리스트로 저장

    return lines

INF = 1e1000

lines = read_txt_lines("/Users/user/Desktop/CodilityStudy/shortest_path/미래도시/input.txt")

N, M = map(int, lines[0].split())

# distance = [[INF] * (N + 1)] * (N + 1)
distance = [[INF] * (N + 1) for _ in range(N + 1)]


vertex_list = []

for line in lines[1:-1]:
    start, end = map(int, line.split())
    vertex_list.append((start, end))

X, K = map(int, lines[-1].split())

for vertex in vertex_list:
    start, end = vertex
    distance[start][end] = 1
    distance[end][start] = 1


def floyd_warshall(distance):
    for k in range(1, N + 1):  # 거쳐가는 노드 k
        for start in range(1, N + 1):  # 시작 노드 start
            for end in range(1, N + 1):  # 도착 노드 end
                distance[start][end] = min(distance[start][end], distance[start][k] + distance[k][end])


floyd_warshall(distance)

print(distance)
print(distance[1][X] + distance[X][K])