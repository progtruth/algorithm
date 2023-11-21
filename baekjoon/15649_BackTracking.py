# https://www.acmicpc.net/problem/15649
# 백트래킹
'''
1. 함수정의 : func(cnt)
	cnt: 현재 수열의 길이
2. base condition
	if cnt == M then 출력
3. 재귀식
	1~N 까지 반복: i
		if i를 수열요소로 선택하지 않았으면,
            cur에 i 추가
            visited[i] = True
            func(cnt+1) 실행
            visited[i] = False
'''

N, M = map(int, input().split())
visited = [False for _ in range(N+1)]
cur = [0 for _ in range(M)]

def func(cnt):
    if cnt == M:
        print(' '.join(map(str, cur)))
        return
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            cur[cnt] = i
            func(cnt + 1)
            visited[i] = False
            
func(0)
