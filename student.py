import sys

def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 65:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"


def main():
    name1 = input()
    name2 = input()

    m1 = int(input())
    m2 = int(input())
    m3 = int(input())

    print(name1)
    print(name2)
    print("Grade", calculate_grade(m1))
    print("Grade", calculate_grade(m2))
    print("Grade", calculate_grade(m3))


if __name__ == "__main__":
    main()