"""Diamond"""
def main(num):
    """loopx2 and print"""
    for row in range(num):
        print(((" "))*(int((num-1)/2)-row), end="")
        if row < (num+1)/2:
            for _ in range((2 * row) + 1):
                print("*", end="")
            print()
    for row in range(int((num+1)/2)-1):
        print(((" "))*(row+1), end="")
        for _ in range(num-2*(row+1)):
            print("*", end="")
        print()
main(int(input()))
