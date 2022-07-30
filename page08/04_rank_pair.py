"""คู่อันดับแบบตามใจฉัน"""
def main(num_i, num_j):
    """loop and print"""
    for stpos in range(1, num_i+1):
        for ndpos in range(1, num_j+1):
            print((stpos, ndpos), end=" ")
        print()
main(int(input()), int(input()))
