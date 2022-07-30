"""x"""
def main(num):
    """loop and print x"""
    for row in range(num):
        for col in range(num):
            if (row == col) or col == num - (row + 1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
main(int(input()))
