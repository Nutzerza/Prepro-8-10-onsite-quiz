"""ถอดรหัสเปลี่ยนโลก"""
def main(txt, word):
    """loop condition print"""
    consonant = [chr(i) for i in range(97, 123)]
    num = []
    ans = ""
    count, count2 = 0, 0
    for i in range(len(word)):
        sum_num = 0
        for j in range(len(word[0])):
            sum_num += consonant.index(word[i][j])
        num.append(sum_num%26)

    for i in range(len(txt)):
        if txt[i] == " ":
            ans += txt[i]
            count2 += 0
        elif txt[i] in consonant:
            ans += consonant[(consonant.index(txt[i]))%26-num[count]]
            if (count2+1) % 3 == 0:
                count += 1
            count2 += 1
        if count % 3 == 0:
            count = 0
    print(ans.capitalize())
main(input().lower(), [input().lower(), input().lower(), input().lower()])
