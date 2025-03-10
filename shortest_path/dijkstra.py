import heapq

def read_txt_lines(path: str) -> list:
    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()  # 전체 줄을 리스트로 저장

    return lines

INF = int(1e9)

lines = read_txt_lines("/Users/visuworks/Desktop/CodilityStudy/shortest_path/input.txt")

n, m = map(int, lines[0].split())

start = int(lines[1].strip())

graph = [[] for i in range(n + 1)]
distance_list = [INF] * (n + 1)

for line in lines[2:]:
    current_node, target_node, distance = map(int, line.split())
    graph[current_node].append((target_node, distance))
    
    
def dijkstra(start):
    # 1. heapq에서 시작노드 담기
    q = []
    heapq.heappush(q, (0, start))
    distance_list[start] = 0
    
    # 2. 돌면서 greedy하게 탐색하기
    while q:
        current_distance, current_node = heapq.heappop(q)
        
        # 이미 확인한 노드는 넘어가기
        if distance_list[current_node] < current_distance:
            continue
        
        for target_node, distance in graph[current_node]:
            cost = current_distance + distance
            if distance_list[target_node] > cost:
                distance_list[target_node] = cost
                heapq.heappush(q, (cost, target_node))
            
            
            
            