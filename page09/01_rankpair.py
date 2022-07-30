"""คู่อันดับ"""
def main(num):
    """loopx2 and print ans"""
    for row in range(num+1):
        for col in range(num+1):
            n_r = str(num-row).zfill(2)
            n_c = str(num-col).zfill(2)
            print("(" + n_r + ", " + n_c + ")", end=" ")
        for col in range(1, num+1):
            n_r = str(num-row).zfill(2)
            print("(" + n_r + ", " + str(col).zfill(2) + ")", end=" ")
        print()

    for row in range(1, num+1):
        for col in range(num+1):
            n_c = str(num-col).zfill(2)
            print("(" + str(row).zfill(2) + ", " + n_c + ")", end=" ")
        for col in range(1, num+1):
            print("(" + str(row).zfill(2) + ", " + str(col).zfill(2) + ")", end=" ")
        print()
main(int(input()))
