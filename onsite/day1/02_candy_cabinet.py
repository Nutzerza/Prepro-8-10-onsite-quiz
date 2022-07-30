"""เบื่อแล้วขนมตู้ อยากเป็นชู้กับเธอ"""
def main(money, water, snack1, snack2, snack3):
    """get value condition print"""
    money_left = money - water
    scr = money_left % 3
    cost = scr == 0 and snack1 * 10 or scr == 1 and snack1 * 15 or scr == 2 and snack1 * 20
    money_left2 = money_left - cost

    scr = money_left2 % 3
    cost2 = scr == 0 and snack2 * 12 or scr == 1 and snack2 * 15 or scr == 2 and snack2 * 18
    money_left3 = money_left2 - cost2

    scr = money_left3 % 3
    cost3 = scr == 0 and snack3 * 5 or scr == 1 and snack3 * 7 or scr == 2 and snack3 * 9
    money_left4 = money_left3 - cost3

    if money_left4 < 0:
        print("Now you have %d left.\nYou don't have enough money!" %money)
    else:
        print("Now you have %d left.\nHere's your order!\nWater: %d baht\nSnack number 1: %d baht\n\
Snack number 2: %d baht\nSnack number 3: %d baht" %(money_left4, water, cost, cost2, cost3))
main(int(input()), int(input()), int(input()), int(input()), int(input()))
