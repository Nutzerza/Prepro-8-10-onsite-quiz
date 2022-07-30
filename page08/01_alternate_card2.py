"""ลองสลับการ์ด แล้วตัดขาดจากใจเธออีกครั้ง"""

def main(times):
    """loop input check print ans yeahhh"""
    card_1, card_2, card_3 = "A", "B", "C"
    for times in range(times):
        change = str(input())
        if change == "12":
            card_1, card_2 = card_2, card_1
        elif change == "13":
            card_1, card_3 = card_3, card_1
        elif change == "21":
            card_2, card_1 = card_1, card_2
        elif change == "23":
            card_2, card_3 = card_3, card_2
        elif change == "31":
            card_3, card_1 = card_1, card_3
        elif change == "32":
            card_3, card_2 = card_2, card_3
        else:
            pass

    print(card_1)
    print(card_2)
    print(card_3)
main(int(input()))
