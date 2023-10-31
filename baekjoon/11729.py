# https://www.acmicpc.net/problem/11729

def hanoi(a, b, n): # 재귀
    if n == 1:
        print(a,b)
        return
    hanoi(a, 6-a-b, n-1)
    print(a,b)
    hanoi(6-a-b, b, n-1)

    
k = int(input())
print(2**k -1)	# 최소 이동횟수
hanoi(1, 3, k)

```
base condition
  n=1일때, a에서 b로 이동 `a b`

재귀함수
  n-1개의 원판을 기둥 a -> 6-a-b로 이동 : `func(a, 6-a-b, n-1)`
  n번 원판을 기둥 a->b로 이동 : `a b`
  n-1개의 원판을 기둥 6-a-b -> b로 이동 : `func(6-a-b, b, n-1)`
```
