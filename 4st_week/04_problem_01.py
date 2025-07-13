import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30

# 현재 재고는 4이고 k = 30일 까지 버텨야 한다.
# 우선 재고 <= k 일때 까지 돌아야 한다.
# 재고 공급량 은 supply_recover[index] <= stock 15까지도 버티는게 가능해 10을 가져와서 stock 에 넣을수 있다.




def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    # 풀어보세요!
    answer = 0
    heap = []
    index = 0

    while stock <= k:
        while index < len(dates) and dates[index] <= stock:
            heapq.heappush(heap, supplies[index])
            index += 1

        supply = heapq.heappop(heap)
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


