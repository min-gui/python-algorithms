input = 20

# 탈출조건 fibo(2) fibo(1) = 1
# fibo(n) = fibo(n-1) + fibo(n-2)
# memo 라는 변수에 Fibo(1)과 Fibo(2) 값을 저장해놨습니다!
memo = {
    1: 1,
    2: 1
}


def fibo_dynamic_programming(n):
    # 구현해보세요!
    if n == 1 or n == 2:
        return 1

    return fibo_dynamic_programming(n - 1) + fibo_dynamic_programming(n -2 )


print(fibo_dynamic_programming(input))


## DP 동적 계획법
## 봉천역 메모이제이션
## 기록한 정보를 이용하면 효율적으로 풀어 볼수 있어