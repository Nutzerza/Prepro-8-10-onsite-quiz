"""บันไดอักษรลง"""
def main(word):
    """get word and print ans"""
    letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = letter.find(word)+1
    for row in range(num):
        for col in range(row+1):
            print(letter[col], end=" ")
        print()
main(input().upper())
