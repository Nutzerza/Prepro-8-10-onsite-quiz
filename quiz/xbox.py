"""Xbox"""
def main(num):
    """print xbox"""
    for row in range(num):
        for col in range(num):
            if (row == col) or (col == (num - 1) - row) or (row == 0)\
                or (col == 0) or (row == num - 1) or (col == num - 1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
main(int(input()))
