"""ตารางสูตรคูณแบบตามใจฉัน"""
def main():
    """loop cal num and print"""
    num_n = int(input())
    num_m = int(input())
    print((("-"))*5)
    for setter in range(2, num_n+1):
        for multiplier in range(1, num_m+1):
            print(setter, "x", multiplier, "=", setter*multiplier, end="\n")
        print((("-"))*5)
main()
