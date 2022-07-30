"""Append"""
def main(num):
    """print list"""
    this_list = []
    for _ in range(num):
        this_list.append(input())
    print('["', end='')
    print(*this_list, sep='", "', end='"]')
main(int(input()))
