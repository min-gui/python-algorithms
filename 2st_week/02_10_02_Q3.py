numbers = [1, 1, 1, 1, 1]
target_number = 3
result = []

def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    # 구현해보세요!
    # 첫번째
    answer = 0
    get_count(array, 0, 0)
    for i in result:
        if i == target:
            answer += 1


    return answer


def get_count(array ,cur_index, cur_sum):
    if cur_index == len(array):
        result.append(cur_sum)
        return

    get_count(array, cur_index + 1, cur_sum + array[cur_index])
    get_count(array, cur_index + 1, cur_sum - array[cur_index])


print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!