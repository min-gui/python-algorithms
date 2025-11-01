from os import fdopen


def solution(s):
    if not s or len(s) == 1:
        return len(s)
    # 최대 비교 개수
    max_len = len(s) // 2
    result_list = []

    for split_size in range(1, max_len + 1):
        split_list = []

        for i in range(0, len(s), split_size):
            split_list.append(s[i:i + split_size])
            pass

        cur_cnt = 1
        result_str = ""
        for i in range(0, len(split_list) - 1):

            cur_str = split_list[i]
            next_str = split_list[i + 1]

            # 문자열 같을때
            if cur_str == next_str:
                cur_cnt += 1
            # 틀릴때
            else:
                if cur_cnt > 1:
                    result_str += f"{cur_cnt}{cur_str}"
                else:
                    result_str += cur_str
                cur_cnt = 1

        if cur_cnt > 1:
            result_str += f"{cur_cnt}{split_list[-1]}"
        else:
            result_str += split_list[-1]

        result_list.append(len(result_str))

    return min(result_list)


if __name__ == "__main__":
    print(solution("abcabcabcabcdededededede"))
    pass
