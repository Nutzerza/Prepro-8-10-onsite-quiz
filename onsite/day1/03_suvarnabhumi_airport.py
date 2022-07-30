"""Suvarnabhumi Airport"""
def main(bkk, abroad, time_bkk):
    """get value condition print"""
    bkk = bkk[-4:-1]
    abr = abroad[-4:-1]
    print(bkk+" - "+abr)

    hour = int(time_bkk[:2])
    minute = int(time_bkk[3:5])
    t_unit = time_bkk[-2:]
    if hour == 12 and (t_unit == "AM" or t_unit == "PM"):
        hour = 0
    if abr == "SYD":
        hour += 12
    elif abr == "SGN":
        hour += 1
        minute += 50
    elif abr == "ATL":
        hour += 9
        minute += 55
    elif abr == "YVR":
        hour += 2
        minute += 20
    elif abr == "KTM":
        hour += 11
        minute += 45

    new_min = [minute // 60, minute % 60]
    hour += new_min[0]
    new_hour = [hour // 12, hour % 12]
    if hour == 12 and t_unit == "AM":
        new_t_unit = "PM"
        new_hour[1] = 12
    elif hour == 12 and t_unit == "PM":
        new_t_unit = "AM"
        new_hour[1] = 12
    elif new_hour[0] == 1 and t_unit == "AM":
        new_t_unit = "PM"
    elif new_hour[0] == 1 and t_unit == "PM":
        new_t_unit = "AM"
    else:
        new_t_unit = t_unit
    print(str(new_hour[1]).zfill(2)+":"+str(new_min[1]).zfill(2)+" "+new_t_unit)
main(input(), input(), input())
