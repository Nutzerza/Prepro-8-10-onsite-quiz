"""ตัวเลขที่มีอยู่"""
def main(lenght):
    """condition loop print"""
    if lenght == 0:
        print("No Tape Measure")
    else:
        ans = 0
        while True:
            txt = input()
            if txt == "No more!":
                break
            elif int(txt) <= lenght:
                ans += int(txt)
        if ans == 0:
            print("Not Found Number")
        else:
            print("Sum of Found Number = %d" %ans)
main(int(input()))
