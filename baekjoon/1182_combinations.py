from itertools import combinations

N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

for n in range(1, N+1):
    for comb in combinations(arr, n):
        if sum(comb) == S:
            cnt += 1
        
print(cnt)
