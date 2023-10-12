# https://www.acmicpc.net/problem/2178
# 미로찾기 (BFS)

from collections import deque

def bfs(rx,ry):
    visited = [[-1]*m for _ in range(n)]
    queue = deque()
    queue.append((rx,ry))
    visited[rx][ry] = 0

    dx, dy = [0,1,0,-1], [1,0,-1,0] 
    
    while queue:
        x,y = queue.popleft()
            
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
            if board[nx][ny] == '0' or visited[nx][ny] >= 0: continue
            queue.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1

    return visited[n-1][m-1] + 1

n,m = map(int, input().split())    # 세로, 가로
global board
board = []
for i in range(n):
    board.append(list(input()))

print(bfs(0,0))