"""โรงเรียนเวทย์มนต์เปิดรับสมัครแล้ว"""
def check_enterschool(age, gen, high):
    """check"""
    if 13 <= age <= 15:
        if (gen == "Male" and high >= 160) or (gen == "Female" and high >= 155):
            return "You can study in junior high school."
        else:
            return "You can not join this school."
    elif 16 <= age <= 18:
        if (gen == "Male" and high >= 170) or (gen == "Female" and high >= 165):
            return "You can study in senior high school."
        else:
            return "You can not join this school."
    else:
        return "You can not join this school."

def main(name, age, gen, high):
    """print ANS"""
    if gen == "Female":
        print("Miss", name, "Age:", age, "Height: %.2f" %high)
    elif gen == "Male":
        print("Mr.", name, "Age:", age, "Height: %.2f" %high)
    print(check_enterschool(age, gen, high))
main(input(), int(input()), input().title(), float(input()))
