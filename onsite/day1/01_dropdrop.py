"""Drop Drop"""
def main(grade):
    """if else print"""
    if grade >= 2:
        print("I\'m so happy.")
    elif grade >= 1:
        print("%.2f" %(4-grade))
    else:
        print("I'm so sad.")
main(float(input()))
