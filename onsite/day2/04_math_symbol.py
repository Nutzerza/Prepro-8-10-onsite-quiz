"""Math Symbol"""
def main():
    """loop condition print"""
    num = []
    while True:
        txt = input()
        if txt == "+" or txt == "-" or txt == "*" or txt == "/":
            varib = txt
            break
        else:
            num.append(int(txt))
    if varib == "+":
        sum_num = num[0] + num[1]
        for i in range(2, len(num)):
            sum_num += num[i]
    elif varib == "-":
        sum_num = num[0] - num[1]
        for i in range(2, len(num)):
            sum_num -= num[i]
    elif varib == "*":
        sum_num = num[0] * num[1]
        for i in range(2, len(num)):
            sum_num *= num[i]
    elif varib == "/":
        sum_num = num[0] / num[1]
        for i in range(2, len(num)):
            sum_num /= num[i]
    print("%.2f" %sum_num)
main()
