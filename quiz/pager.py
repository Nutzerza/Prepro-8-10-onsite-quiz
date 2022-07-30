"""Pager"""
def main(ren):
    """cal num print ans"""
    txt20 = [ren // 20, ren % 20]
    txt8 = [txt20[1] // 8, txt20[1] % 8]
    txt3 = [txt8[1] // 3, txt8[1] % 3]
    txt1 = [txt3[1] // 1]
    cost = (18.5*txt20[0]) + (6.5*txt8[0]) + (3*txt3[0]) + (1.5*txt1[0])
    print("Text's length is : "+'"%d"' %ren)
    print("Total price is   : %.2f Baht\\.-" %cost)
main(len(input()))
