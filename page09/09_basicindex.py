"""Basic Index"""
def main():
    """loop append list print ans"""
    this_list = []
    while True:
        txt = str(input())
        if txt.title() == "End":
            break
        else:
            this_list.append(txt)
    num = int(input())
    if len(this_list) <= num:
        print("Index Not Found")
    else:
        print("List[" + str(num) + '] = "'+this_list[num]+'"')
main()
