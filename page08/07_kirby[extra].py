"""[Extra] KIRBY Adventure - 01 [HELP!]"""
def check_role(role):
    """check role and return atk kirby"""
    if role == "Sword":
        return 4
    elif role == "Magic":
        return 2
    elif role == "Sleep":
        return 0
    elif role == "Master":
        return 9

def atk_phase(hp_kirby, atk_kirby, enemies):
    """cal hp kirby behind enemies atk"""
    ene_name = ""
    if enemies == "Waddle Dee":
        atk_ene, hp_ene = 1, 2
        ene_name = "Waddle Dee"
    elif enemies == "Laser Ball":
        atk_ene, hp_ene = 2, 3
        ene_name = "Laser Ball"
    elif enemies == "Waddle Doo":
        atk_ene, hp_ene = 3, 5
        ene_name = "Waddle Doo"
    if hp_kirby > 0:
        hp_kirby = hp_kirby - atk_ene
        if hp_kirby > 0:
            hp_ene = hp_ene - atk_kirby
            if hp_ene <= 0:
                print("-", ene_name.lower(), "had defeated -\n%d HP left\n" %hp_kirby + (("-"))*12)
            elif hp_ene > 0:
                print("%d HP left\n" %hp_kirby + (("-"))*12)
    return hp_kirby

def ene_heal(hp_kirby, atk_kirby, enemies):
    """check hp enermies behind kirby atk"""
    if enemies == "Waddle Dee":
        atk_ene, hp_ene = 1, 2
    elif enemies == "Laser Ball":
        atk_ene, hp_ene = 2, 3
    elif enemies == "Waddle Doo":
        atk_ene, hp_ene = 3, 5
    if hp_kirby > 0:
        hp_kirby = hp_kirby - atk_ene
        hp_ene = hp_ene - atk_kirby
    return hp_ene

def main(hp_kirby):
    """get value check and print won lose """
    def_ene = 0
    while True:
        print((("-"))*12)
        atk_kirby = check_role(input().title())
        enemies = input().title()
        if enemies == "Waddle Dee" or enemies == "Laser Ball" or enemies == "Waddle Doo":
            hp_kirby = atk_phase(hp_kirby, atk_kirby, enemies)
            hp_ene = ene_heal(hp_kirby, atk_kirby, enemies)
            if hp_kirby > 0 and hp_ene <= 0:
                def_ene += 1
        elif enemies == "Heal":
            hp_kirby += 2
            print(hp_kirby, "HP left\n"+(("-"))*12)
        elif enemies == "None":
            print(hp_kirby, "HP left")
            print("Kirby won!\nYou had defeated %d enemies\n" %def_ene + (("-"))*12)
            break
        if hp_kirby <= 0:
            print(hp_kirby, "HP left")
            print("GameOver!\nYou had defeated %d enemies\n" %def_ene + (("-"))*12)
            break
main(int(input()))
