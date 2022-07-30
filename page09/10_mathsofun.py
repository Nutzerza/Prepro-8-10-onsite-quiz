"""คณิตพาเพลิน"""
def main(num):
    """get value print ans"""
    thislist = []
    for _ in range(num):
        thislist.append(float(input()))
    muti = float(input())
    for count in range(len(thislist)):
        thislist.insert(count, "%.2f" %(thislist[count]*muti))
        thislist.pop(count + 1)
    print(thislist)
main(int(input()))
