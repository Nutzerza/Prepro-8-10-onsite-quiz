"""นาฬิกาทราย"""
def main(num):
    """loop and prind ans"""
    print((("*"))*(num*2+1))
    for row in range(num*2+1):
        for col in range(num*2+1):
            if (row == col) or (col == (num*2+1)-(row+1)):
                print("*", end="")
            else:
                print(" ", end="")
        print()
    print((("*"))*(num*2+1))
main(int(input()))
