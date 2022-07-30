"""เกมวิ่งเก็บ"""
def main(txt):
    """loop print"""
    pos = 0
    sum_range = 0
    for i in range(0, len(txt)):
        sum_range += abs(float(txt[i]) - pos)
        pos = float(txt[i])
    print("%.2f" %sum_range)
main(input().split())
