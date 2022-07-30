"""บันไดแมว"""
def main(num):
    """loop and print ans"""
    for row in range(num):
        for _ in range(row):
            print(" ", end=" ")
        print((("* "))*(num-row), end=" ")
        print()
main(int(input()))
