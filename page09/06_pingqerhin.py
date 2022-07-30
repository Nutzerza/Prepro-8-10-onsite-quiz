"""ปิงฉีหลิน"""
def main(num, txt):
    """check loop and print"""
    if txt == "m" or txt == "s" or txt == "c" or txt == "b" or txt == "r":
        for row in range(num):
            print(((" "))*(num-(row+1)), end="")
            for _ in range((2*row)+1):
                print(txt, end="")
            print()
        for row in range(num-1):
            print(((" "))*(row+1), end="")
            for _ in range(num*2-(2*(row+1)+1)):
                print("_", end="")
            print()
    else:
        print("Hey!,buy another shop.")
main(int(input()), str(input().lower()))
