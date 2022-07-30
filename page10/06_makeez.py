"""ทำให้ดูง่าย"""
def main(num):
    """"""
    jop_list = []
    name_age = []
    for _ in range(num):
        jop_list.append(input())
    for counter in range(len(jop_list)):
        name_age.append(jop_list[counter][0:jop_list[counter].find(" ")])
    # print(jop_list[1].find(" "))
    print(name_age)
main(int(input()))
