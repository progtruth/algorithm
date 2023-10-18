# 7576 토마토
# 익은토마토 옆에 있는 토마토는 하루가 지나면 익음

from collections import deque

def bfs():
    dx, dy = [0,1,0,-1], [1,0,-1,0]
    q = deque()
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                q.append([i, j])
    days = 0
    while not check_tomatos():
        if not q:
            return -1
            
        cnt = len(q)
        plus = False
        for _ in range(cnt):
            x,y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
                if board[nx][ny] == 0:
                    board[nx][ny] = 1
                    q.append([nx,ny])
                    plus = True
        days += plus
        print(days, "일 후")
        for i in range(N):
            print(board[i])
        print(q)
                  
    return days

def check_tomatos():
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                return False
    return True

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

print(bfs())