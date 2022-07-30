"""Simple matrix"""
def main(num_1, num_2):
    """get value loop print ans"""
    for row in range(num_1):
        for col in range(row+1, (num_2*(row+1))+1, row+1):
            print(col, end=" ")
        print()
main(int(input()), int(input()))
