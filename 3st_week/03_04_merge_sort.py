array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


def merge(array1, array2):
    result = []
    array1_size = len(array1)
    array2_size = len(array2)
    array1_idx = 0
    array2_idx = 0

    while (array1_size > array1_idx and array2_size > array2_idx):
        val_1 = array1[array1_idx]
        val_2 = array2[array2_idx]

        if (val_1 < val_2):
            result.append(val_1)
            array1_idx += 1
        else:
            result.append(val_2)
            array2_idx += 1


    temp_arr = None
    temp_idx = None
    if(array1_size <= array1_idx):
        temp_arr = array_b
        temp_idx = array2_idx
    else:
        temp_arr = array_a
        temp_idx = array1_idx

    while (len(temp_arr) > temp_idx):
        result.append(temp_arr[temp_idx])
        temp_idx += 1


    return result


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge([-7, -1, 9, 40], [5, 6, 10, 11]))
print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge([-1, 2, 3, 5, 40], [10, 78, 100]))
print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge([-1, -1, 0], [1, 6, 9, 10]))
