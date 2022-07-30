"""Minesweeper"""
def main(ren):
    """"""
    bomb = []
    for a in range(int(input())):
        bomb.append(input())
    print(bomb)
    for i in range(int(ren[0])):
        for j in range(int(ren[2])):
            print("0", end=" ")
        print()
main(input())
