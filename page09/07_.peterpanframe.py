"""PeterPanframe"""
def line_one(num):
    """print line 1"""
    for count in range(1, num+1):
        if count % 3 == 0:
            print("..◊.", end="")
        else:
            print("..♦.", end="")
    print(end=".\n")

def line_two(num):
    """print line 2"""
    for count in range(1, num+1):
        if count % 3 == 0:
            print(".◊.◊", end="")
        else:
            print(".♦.♦", end="")
    print(end=".\n")

def line_three(txt):
    """print line 3"""
    counter = 0
    print("♦", end="")
    for character in txt:
        counter += 1
        print(".%s." %character, end="")
        if counter % 3 == 1:
            print("♦", end="")
        else:
            print("◊", end="")
    print(end="\n")

def main(txt):
    """call function"""
    num = len(txt)
    line_one(num)
    line_two(num)
    line_three(txt)
    line_two(num)
    line_one(num)
main(input())
