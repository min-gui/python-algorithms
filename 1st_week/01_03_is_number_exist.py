# 빅오 -> 최악의 경우.
# 빅오메가 -> 최선의 경우.

def is_number_exist(number, array):
    for element in array:  # array 의 길이만큼 아래 연산이 실행
        if number == element:  # 비교 연산 1번 실행
            return True  # 시간복잠도는 N만큼 걸린다.
    return False


result = is_number_exist
print("정답 = True 현재 풀이 값 =", result(3, [3, 5, 6, 1, 2, 4]))
print("정답 = Flase 현재 풀이 값 =", result(7, [6, 6, 6]))
print("정답 = True 현재 풀이 값 =", result(2, [6, 9, 2, 7, 1888]))

print(ord("a"))
print(chr(97))

input = input()
def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_one = 0
    count_zero = 0

    if string[0] == '1':
        count_zero += 1
    elif string[0] == '0':
        count_one += 1

    for i in range(len(string) - 1):
        if string[i] != string[i + 1]:
            if string[i + 1] == '1':
                count_zero += 1
            elif string[i + 1] == '0':
                count_one += 1
    print('----')
    print(min(count_one, count_zero))


find_count_to_turn_out_to_all_zero_or_all_one(input)