input = [4, 6, 2, 9 ,1]


def bubble_sort(array):
    # 이 부분을 채워보세요!

    search_len = len(input)
    row_cnt = 1;

    while(search_len > 1):

        a = input[row_cnt -1]
        b = input[row_cnt]

        if (a > b):
            input[row_cnt -1] = b
            input[row_cnt] = a


        if(row_cnt == search_len - 1):
            search_len -= 1
            row_cnt = 1
            continue

        row_cnt += 1



    return array


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",bubble_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",bubble_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",bubble_sort([100,56,-3,32,44]))