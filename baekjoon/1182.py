# 백트래킹
import sys
sys.setrecursionlimit(2**30)

N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

def func(idx, cur_sum):
    global cnt
    if idx == N:
        if cur_sum == S:
            cnt += 1
        return	# return 들여쓰기 주의!!! (메모리초과 오류발생)
    func(idx+1, cur_sum)
    func(idx+1, cur_sum + arr[idx])


func(0, 0)
# 크기가 양수인 부분수열 중에서
if S == 0: # 공집합 제외
    cnt -= 1
print(cnt)

'''
N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.

1. 함수정의 ; func(idx, cur_sum)
	idx번째 수를 더할지말지 결정하기
	만약 idx번째수가 N번째 수라면, S == cur_sum 인지 확인하기
2. base condition
	if idx == N:
		if cur_sum == S:
			cnt += 1
		return
3. 재귀식
	1~N번째 수에 대해서 (idx)
		idx번째 수를 선택안하면, func(idx+1, cur_sum)
		idx번째 수를 선택하면, func(idx+1, cur_sum + arr[idx])
'''

