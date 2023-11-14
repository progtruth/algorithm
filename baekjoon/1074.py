def func(n, r, c):
    if n == 0: 
        return 0
        
    half = 2**(n-1)
    if r < half and c < half: # 1번사각형
        return func(n-1, r, c)
    if r < half and c >= half: # 2번사각형
        return half*half + func(n-1, r, c-half)
    if r >= half and c < half: # 3번사각형
        return 2*half*half + func(n-1, r-half, c)
    return 3*half*half + func(n-1, r-half, c-half) # 4번사각형

    
N, r, c = map(int, input().split())
print(func(N, r, c))

'''
재귀 사용

1. 함수 정의
   def func(n, r, c) : 2^n X 2^n 배열에서 (r행 c열) 을 방문하는 순서를 반환하는 함수
2. base condition
   n=0일때, return 0
3. 재귀식
'''
