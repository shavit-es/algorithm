from collections import deque

def bfs(graph, start, visited):
  queue = deque([start]) #큐(queue) 구현을 위해 deque 라이브러리 사용
  visited[start] = True #현재 노드를 방문 처리
  while queue: #큐가 빌 때까지 반복
    v = queue.popleft()
    print(v, end=' ')
    for i in graph[v]:#해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
      if not visited[i]:
        queue.append(i)
        visited[i] = True