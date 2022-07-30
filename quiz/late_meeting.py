"""Late Meeting"""
def main(hour, min_clock, sec_clock, period, min_friend, sec_friend):
    """print ans"""
    sum_sec = sec_clock + sec_friend
    sum_min = min_clock + min_friend
    set_sec = [sum_sec // 60, sum_sec % 60]
    if set_sec[0] > 0:
        sum_min += set_sec[0]
    set_min = [sum_min // 60, sum_min % 60]
    if set_min[0] > 0:
        hour += set_min[0]

    if (hour == 12 and set_min[1] == 0 and set_sec[1] == 0) and (period == "am"):
        period = "pm"
    elif hour >= 12 and period == "am":
        hour = hour % 12
        period = "pm"
    elif (hour == 12 and set_min[1] == 0 and set_sec[1] == 0) and period == "pm":
        period = "am"
    elif hour >= 12 and period == "pm":
        hour = hour % 12
        period = "am"
    # print(hour, set_min[1], set_sec[1], period)
    txt = "{}:{}:{} {}".format(str(hour).zfill(2), str(set_min[1]).zfill(2), str(set_sec[1]).zfill(2), period)
    print(txt)
main(int(input()), int(input()), int(input()), input().lower(), int(input()), int(input()))

#19/68
#9,10,11,12,16,17,18,22,23,24,25,28,29,30,31,42,43,54,55
