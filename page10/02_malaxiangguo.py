"""Mala xiang guo"""
def main():
    """loop condition print"""
    food_item = []
    check = []
    spi_num = 0
    food_list = ["celery stalks", "carrots", "potatoes", "mushrooms", "tofu", "lotus root"\
        , "cabbage", "instant noodles", "glass noodle", "wonton", "beef", "pork loin"\
        , "chicken", "fish balls", "cheese ball", "octopus", "fish", "shrimp", "mussels"]
    spicy = ["Mild", "Medium", "Hot", "Extra hot"]
    while True:
        txt = input().lower()
        if txt == "stop":
            break
        elif txt == "1" or txt == "2" or txt == "3" or txt == "4":
            spi_num = int(txt)
        else:
            food_item.append(txt)
    if len(food_item) == 0:
        print("Huh? you didn't order anything!")
    elif spi_num == 0:
        print("Please choose a spicy level!")
    else:
        for i in range(len(food_item)):
            if food_item[i] in food_list:
                pass
            else:
                check.append("Get out!")
        if "Get out!" in check:
            print("Get out!")
        else:
            print(spicy[spi_num-1], "Mala xiang guo is here.")
main()
