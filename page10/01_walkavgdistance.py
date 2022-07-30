"""Walking average distance"""
import math
def main(day):
    """loop append list print ans"""
    step_num = []
    avg = 0
    for pos in range(day):
        step_num.append(int(input()))
        avg = avg + step_num[pos]
    avg = avg / day
    for num in step_num:
        if num > avg:
            ans = num - avg
        else:
            ans = avg - num
        print(math.ceil(ans))
main(int(input()))
