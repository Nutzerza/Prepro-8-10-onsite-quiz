"""หมอบกู๋"""
def main(money_have):
    """cal num sheck print"""
    low_cost = 100
    lowest_shop = 1
    for shop in range(1, 11):
        for _ in range(5):
            cost = float(input())
            if cost <= money_have:
                break
            elif cost > money_have:
                if low_cost >= cost:
                    low_cost, cost = cost, low_cost
                    lowest_shop = shop
                elif low_cost < cost:
                    low_cost = low_cost
        if cost <= money_have:
            print("%.2f" %cost)
            print(shop)
            break
        if shop == 10:
            print("%.2f" %low_cost)
            print(lowest_shop)
main(float(input()))
