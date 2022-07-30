"""คู่อันดับ"""
def main(num):
    """loop and print ans"""
    for row in range(num):
        print((("  "))*((num-1)-row), end="")
        for _ in range((2 * row) + 1):
            print("*", end=" ")
        print()
main(int(input()))
