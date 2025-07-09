import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30
# stock 기존 재고량
# stock 4개 있다 나는 4일 까지 버틸 수 있고 4일 안에서 최대 량을 뽑아서 나오면 된다.


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    # 풀어보세요!
    answer = 0
    heap = []
    index = 0

    while stock <= k:
        while index < len(dates) and dates[index] <= stock :
            heapq.heappush(heap, supplies[index] * -1)
            index += 1 # 아 2틀 까지 가면 그뒤는 다시 볼 필요 없어서....

        supply = heapq.heappop(heap) * -1
        stock += supply
        answer += 1

    return answer

print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))

print("정답 = 2 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15], [20, 5, 10], 30))
print("정답 = 4 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15, 20], [20, 5, 10, 5], 40))
print("정답 = 1 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(2, [1, 10], [10, 100], 11))


testHeap = []

heapq.heappush(testHeap, 10)
heapq.heappush(testHeap, 15)
heapq.heappush(testHeap, 8)
heapq.heappush(testHeap, 7)
heapq.heappush(testHeap, 11)
heapq.heappush(testHeap, -11)
heapq.heappush(testHeap, 11)


