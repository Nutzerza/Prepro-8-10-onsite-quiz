"""ความรักคือการหมุนรอบกัน ไม่ใช่ให้เธอหมุนรอบฉัน หรือให้ฉันหมุนรอบใคร"""
def main(spin, num_line):
    """loop list print"""
    list_txt = []
    for i in range(num_line):
        list_txt.append(input())
    for pos in range(len(list_txt)):
        if len(list_txt[-1]) != len(list_txt[pos]):
            print("Invalid size")
            break
        else:
            if spin == "90":
                for i in range(len(list_txt[0])):
                    for j in range(len(list_txt)):
                        print(list_txt[-j-1][i], end="")
                    print()
                break
            elif spin == "180":
                for i in range(len(list_txt)):
                    print(list_txt[-i-1][::-1])
                break
            elif spin == "flip":
                for i in range(len(list_txt)):
                    print(list_txt[i][::-1])
                break
main(input(), int(input()))
