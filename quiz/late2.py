"""Late Meeting"""
def main(sum_hour, min_clock, sec_clock, period, min_friend, sec_friend):
    """print ans"""
    sum_sec = sec_clock + sec_friend
    sum_min = min_clock + min_friend

    sec = sum_sec % 60
    sum_min += sum_sec // 60
    minute = sum_min % 60
    sum_hour += sum_min // 60
    if sum_hour == 12 and period == "pm":
        hour = 12
        period = "am"
    elif sum_hour == 12 and period == "am":
        hour = 12
        period = "pm"
    elif sum_hour < 12:
        hour = sum_hour
    elif sum_hour > 12 and period == "am":
        hour = sum_hour % 12
        period = "pm"
    elif sum_hour > 12 and period == "pm":
        hour = sum_hour % 12
        period = "am"
    print(str(hour).zfill(2)+":"+str(minute).zfill(2)+":"+str(sec).zfill(2), period)

main(int(input()), int(input()), int(input()), input().lower(), int(input()), int(input()))

# 16/68
#9,10,11,12,16,17,22,23,24,25,28,29,30,31,43,55

