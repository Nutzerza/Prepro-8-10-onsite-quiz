"""Ranking the scores"""
def main(numinput):
    """get value loop sort index print"""
    print(sorted(numinput))
    sot = sorted(numinput)
    sot.reverse()
    numoutput = []
    for num in numinput:
        numoutput.append(sot.index(num)+1)
    print(*numoutput, sep=",")
main(input().split(","))
