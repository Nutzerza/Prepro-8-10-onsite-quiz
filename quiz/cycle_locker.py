"""Cycle Locker"""
def main(st_num, nd_num):
    """loop check print ans"""
    ans = 0
    for i in range(len(st_num[:4])):
        if abs(int(st_num[i]) - int(nd_num[i])) <= 5:
            num = abs(int(st_num[i]) - int(nd_num[i]))
            ans += num
        elif abs(int(st_num[i]) - int(nd_num[i])) > 5:
            num = 10 % abs(int(st_num[i]) - int(nd_num[i]))
            ans += num
    print(ans)
main(input(), input())

# if num == 0 and st_num[i] != nd_num[i]:
#                 ans += 5
#             else:
#                 ans += num
