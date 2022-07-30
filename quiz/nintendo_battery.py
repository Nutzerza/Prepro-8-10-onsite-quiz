"""Nintendo Battery"""
def main(percent, ren):
    """get value & print ans"""
    num = int(ren * percent)
    txt = ("("+(("O"))*num+(("_"))*(ren-num)+") {:.0%}")
    print(txt.format(percent))
main(int(input())/100, int(input()))
