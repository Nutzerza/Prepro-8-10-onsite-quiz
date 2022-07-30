"""Atbash Cipher"""
def main(txt):
    """loop print"""
    new = ""
    for i in range(len(txt)):
        if ord(txt[i]) >= 97:
            ch_txt = ord(txt[i]) - 96
            new += chr(123 - ch_txt)
        elif ord(txt[i]) >= 65:
            ch_txt = ord(txt[i]) - 64
            new += chr(91 - ch_txt)
        else:
            new += txt[i]
    print(new)
main(input())
