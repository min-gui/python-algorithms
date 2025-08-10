from collections import deque

print("인턴쉽 문제 시작")

# 게임이 끝나는 최소시간 구하기.
# 브라운 이 코니를 잡거나, 코니가 너무 멀리 벗어나면 끝나는 게임
# 너무 멀리 벗어났다는것을 어떻게 판단 할 것인가 ?
# 코니는 처음 위치에서 1초후 1만큼 움직임.
# 이전 이동거리 +1 만큼 움직인다 = 가속
# 1, 2, 4, 7
# c , c+1, c+1+2,
# 코니 조건 부터 먼저 생각하자
# C , C+1, C+2+1, C+3+3, C+4+6
# 11, 12 , 14, 17
# 처음, 이동거리, (C+2) 분(이전), (C+3) (2+1),(C+4) (3+3)
# 점화식
# 조건 0 <= x <= 200,000 위치
# 코니가 범위를 벗어나면 게임 끝
# 브라운은 무조건 2*B 로 가는게 최선 아닌가 ?

from collections import deque

c = 11
b = 2


# 문제 설명을 정확히 읽는게 중요하다.


def catch_me(cony_loc, brown_loc):
    time = 0
    queue = deque()
    queue.append((brown_loc, 0))
    #dictionary 로 한 이유는 키값으로 찾을려고 dictionary로 했음.
    # 해당 위치에 도달했을때 몇초 였는지 기록하기 위한것.
    visitied = [{} for _ in range(200001)] #20만 개를 넣어 놓는다.


    while cony_loc < 200000:
        # 코니의 위치는 최종적으로 아래와 같이 변한다.
        # 시간 순서대로 변하기 때문에 시간에 증가함에 따랄 시간 만큼 증가.
        # 11 , 12 , 14, 17 , 21
        cony_loc += time

        # 코니의 위치가 시간에 있다면
        # 코니의 시간이 기준이 되기 때문에 가능
        if time in visitied[cony_loc]:
            #이시간이 서로 만나는 시간
            return time


        # 10 이라는 위치에 도달 했던게 1초 10초 600초 700초
        # [10][1, 10, 600, 700]

        # 위치 10 에 도달한 시간 4때 도달
        # 예) visitied[10] = {시간 : TRUE}

        # 브라운의 위치는 경우의 수가 다양하다.
        # 브라운의 위치는 bfs 이용하자 .
        for i in range(0, len(queue)): # while queue를 안쓰고 for 문을 쓸까요?
            current_position, current_time = queue.popleft()

            new_time = current_time + 1
            new_position = current_position -1

            if 0 <= new_position <= 200000:
                visitied[new_position][new_time] = True
                queue.append((new_position,new_time)) # brown_loc - 1, 1


            new_position = current_position +1
            if 0 <= new_position <= 200000:
                visitied[new_position][new_time] = True
                queue.append((new_position,new_time)) # brown_loc + 1, 1


            new_position = current_position *2
            if 0 <= new_position <= 200000:
                visitied[new_position][new_time] = True # visited[new_position][new_time]
                queue.append((new_position,new_time)) # brown_loc * 2, 1
        time += 1


print(catch_me(c, b))  # 5가 나와야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", catch_me(10, 3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51, 50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550, 500))


# 코니는 시간마다 늘어난다 이전 값 을 더해서 11 12 14 17 21
# 브라운은 시간오면 해단 시간에 갈 수 있는 모든 경우의 수를 탐색 해서 넣는다.
# queue에는 다음 경우의 수를 계산하기 위해서 넣는다. 1-1-1 1-1-2 1-1-3 -> 1-1-1-1, 1-1-1-2, 1-1-1-3 -> 1-1-1-1-1,1-1-1-1-2,1-1-1-1-3 이런식으로 bfs 늘어 나기 위
# 첫번째는 브라운위치는 2 이니깐 1위치에 1시간 True, 3위치에 1시간 true, 4위치에 1시간 true