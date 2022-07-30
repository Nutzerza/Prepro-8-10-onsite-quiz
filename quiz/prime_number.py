"""Prime Number"""
import math

def main(num):
    """check Prime Number"""
    if num > 1 and (math.factorial(num-1)+1) % num == 0:
        print("Prime Number")
    else:
        print("Not Prime Number")

main(int(input()))
