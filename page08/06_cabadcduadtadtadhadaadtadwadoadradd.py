"""cabadcduadtadtadhadaadtadwadoadradd"""
def main(txt):
    """get value loop print"""
    while True:
        word = input().lower()
        counter = txt.count(word)
        if txt.find(word) == -1:
            break
        else:
            for _ in range(counter):
                txt = txt.replace(word, "")
    print(txt)
main(input().lower())
