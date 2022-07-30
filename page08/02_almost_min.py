"""อันดับสองรองสุดท้าย"""
def main():
    """input check loop print ans"""
    num_1, num_2 = int(input()), int(input())
    if num_1 > num_2:
        num_1, num_2 = num_2, num_1
    for _ in range(8):
        value = int(input())
        if value < num_1:
            num_1, num_2 = value, num_1
        elif num_1 < value < num_2:
            num_2 = value
    print("Almost the min :", num_2)

main()
