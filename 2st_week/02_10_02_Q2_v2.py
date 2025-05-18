shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "라라"]


def is_available_to_order(menus, orders):
    menus_set = set(menus)
    for order in orders:
        if order not in menus_set:
            return False
    return True


def search(item, menus):
    min = 0
    max = len(menus) - 1
    menus.sort()

    while min <= max:
        mid = (min + max) // 2
        if menus[mid] == item:
            return True
        elif menus[mid] > item:
            max = mid - 1
        elif menus[mid] < item:
            min = mid + 1

    return False



result = is_available_to_order(shop_menus, shop_orders)
print(result)
