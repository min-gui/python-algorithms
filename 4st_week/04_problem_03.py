seat_count = 9
vip_seat_array = [4, 7]

# 예전에 만들었던 fibo_dynamic_programming 에서 가져오면 됩니다!
memo = {
    1: 1,  # 이 문제에서는 Fibo(1) = 1, Fibo(2) = 2 로 시작합니다!
    2: 2
}


def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = nth_fibo
    return nth_fibo


def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    all_ways = 1
    current_index = 0

    for fixed_seat in fixed_seat_array:
        fixed_seat_index = fixed_seat - 1
        count_of_ways = fibo_dynamic_programming(fixed_seat_index - current_index, memo)
        all_ways *= count_of_ways
        current_index = fixed_seat_index + 1

    count_of_ways = fibo_dynamic_programming(total_count - current_index, memo)
    all_ways *= count_of_ways
    return all_ways


# print(fibo_dynamic_programming(5, memo))
# # 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))

print("정답 = 4 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(9, [2, 4, 7]))
print("정답 = 26 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(11, [2, 5]))
print("정답 = 6 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(10, [2, 6, 9]))

print("------")


def fibo_dp(n):
    # 초기 변수 선언
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n];


def get_all_ways_of_theater_seatV2(total_count, fixed_seat_array):
    all_ways = 1
    prev_seat = 0
    for fixed_seat in fixed_seat_array:
        move_size = fixed_seat - (prev_seat+1)
        all_ways *= fibo_dp(move_size)
        prev_seat = fixed_seat
    # 마지막 행과 total_count 까지
    seat = total_count - prev_seat
    all_ways *= fibo_dp(seat)



    return all_ways


print(get_all_ways_of_theater_seatV2(seat_count, vip_seat_array))
print("정답 = 4 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(9, [2, 4, 7]))
print("정답 = 26 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(11, [2, 5]))
print("정답 = 6 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(10, [2, 6, 9]))