"""โดนใยแมงมุม เหมือนโดนเธอกุมหัวใจ"""
def main(num):
    """loop codition print"""
    for i in range(-num, num+1):
        for j in range(-num, num+1):
            if i == 0 or j == 0 or  abs(i) == abs(j) or abs(i) % 2 != 0 and abs(j) <= abs(i)\
            or abs(j) % 2 != 0 and abs(i) <= abs(j):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
main(int(input()))
