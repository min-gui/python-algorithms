from collections import deque

current_r, current_c, current_d = 7, 4, 0
current_room_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


# 청소한 공간도 기록해야된다. 그런 맵이 두개 있어야 된다.
# r,c 위치 d 바라보는 방향 , 그리고 방향은 왼쪽부터 , 위 ,오른쪽 ,아래
# a. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.
# b. 왼쪽 방향에 청소할 공간이 없다면, 그 방향으로 회전하고 2번으로 돌아간다.
# c. 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
# d. 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에

def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    # d 가 0 이면 북쪽 1이면 오른쪽 2이면 남쪽 3이면 왼쪽
    # 정사각형인데 우선 r은 x축 c는 y축으로 생각하자
    # d가 0이면 x축은 -1, y축은 0 으로

    n = len(room_map) #c 에 대한 길이
    m = len(room_map[0]) #r 에 대한 길이

    room_map[r][c] = 2
    cnt_cleand = 1
    queue = deque([[r, c, d]])
    # 나아갈 방향이다
    direct = [[0, -1], [1 , 0], [0, 1], [-1, 0]]

    while queue:
        r, c, d = queue.popleft()
        temp_d = d
        # 서쪽을 탐색 할 수 있을지 없을지 탐색
        for i in range(4):
            temp_d = get_d_index_when_rotate_to_left(temp_d)  # 북 -> 서
            new_r, new_c = r + direct[temp_d][1], c + direct[temp_d][0]
            # a. 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행한다.

            if 0 <= new_c < n and 0 <= new_r < m and room_map[new_r][new_c] == 0:
                cnt_cleand += 1
                room_map[new_r][new_c] = 2
                #청소 했고, 해당위치에서 다시 시작하고 싶어서 아래에 넣어준다.
                queue.append([new_r, new_c, temp_d])
                break

            # c. 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸 후진을 하고 2번으로 돌아간다.
            elif i == 3:
                temp_d = get_d_index_when_go_back(d)
                new_r, new_c = r + direct[temp_d][1], c + direct[temp_d][0]
                ##여기서 조건문이 추가 되어야 한다. 후진 했을때 범위를 넘어가거나 여전히 막혀 있을때
                # 방향을 유지한채 니깐 d
                queue.append([new_r, new_c, d])
                if room_map[new_r][new_c] == 1:
                    return  cnt_cleand

    return cnt_cleand


## 0(북) = 3 , 1(동) = 0 , 2(남) = 1, 3(서) = 2
def get_d_index_when_rotate_to_left(d):
    return (d + 3) % 4


def get_d_index_when_go_back(d):
    return (d + 2) % 4

# 57 가 출력되어야 합니다!
print(get_count_of_departments_cleaned_by_robot_vacuum(current_r, current_c, current_d, current_room_map))
current_room_map2 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
print("정답 = 29 / 현재 풀이 값 = ", get_count_of_departments_cleaned_by_robot_vacuum(6, 3, 1, current_room_map2))
current_room_map3 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
print("정답 = 33 / 현재 풀이 값 = ", get_count_of_departments_cleaned_by_robot_vacuum(7, 4, 1, current_room_map3))
current_room_map4 = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
print("정답 = 25 / 현재 풀이 값 = ", get_count_of_departments_cleaned_by_robot_vacuum(6, 2, 0, current_room_map4))
# r 의값 c의 값 대로 그대로 풀자 헷갈린다 r은 세로축, c은 가로축