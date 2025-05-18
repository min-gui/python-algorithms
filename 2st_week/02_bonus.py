# 3번째 인덱스를 찾아서 순회한다.
# list 가 0이면 종료 해야 한다.
def josephus_problem(n, k):
    # 이 부분을 채워보세요!
    index = k - 1
    p_list = list(range(1, n + 1))
    result_list = []

    while p_list:
        list_append = p_list.pop(index)
        result_list.append(list_append)
        #0으로 나누면 ZeroDivisionError 에러 발생
        if(index != 0):
            index = (index + (k - 1)) % len(p_list)


n, k = map(int, input().split())
josephus_problem(n, k)
