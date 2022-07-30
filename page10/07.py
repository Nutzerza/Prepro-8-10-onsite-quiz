"""น้ำอัดลมทำให้ผมชอบเรอ น่ารักแบบเธอทำให้ผมชอบใจ"""
def check_water(check, cost):
    """check water"""
    if "Invalid order!" in check:
        print("Invalid order!")
    elif "soft" in check:
        print("Here\'s your soft drink!\nCost %d baht." %cost)
    else:
        print("Here\'s your juice!\nCost %d baht." %cost)

def main():
    """loop condition print"""
    water = []
    check = []
    cup_ice = ["cup", "ice"]
    fruit = ["orange", "banana", "strawberry", "cherrie", "watermelon", "lemon", "mango", "grape"]
    price_fru = [17, 13, 10, 15, 12, 19, 21, 11]
    cost = 0
    while True:
        txt = input().lower()
        if txt == "end":
            break
        else:
            water.append(txt)
    if water[0] != "cup" or water[-1] != "ice":
        print("Invalid order!")
    else:
        for i in range(len(water)):
            if water[i] == "coke" or water[i] == "pepsi" or\
                water[i] == "sprite" or water[i] == "fanta":
                check.append("soft")
                cost += 15
            elif water[i] in cup_ice:
                cost += 5
            elif water[i] in fruit:
                for j in range(len(fruit)):
                    if water[i] == fruit[j]:
                        cost += price_fru[j]
            else:
                check.append("Invalid order!")
        check_water(check, cost)
main()
