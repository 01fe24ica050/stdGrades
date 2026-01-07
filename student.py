def main():
    try:
        import sys
        name = sys.argv[1]
        m1 = int(sys.argv[2])
        m2 = int(sys.argv[3])
        m3 = int(sys.argv[4])
    except (IndexError, ValueError):
        # Ask user interactively if not enough arguments
        name = input("Enter student name: ")
        m1 = int(input("Enter marks 1: "))
        m2 = int(input("Enter marks 2: "))
        m3 = int(input("Enter marks 3: "))

    total = m1 + m2 + m3
    avg = total / 3
    print(f"Name: {name}")
    print(f"Marks: {m1} {m2} {m3}")
    print(f"Total: {total}")
    print(f"Average: {avg}")

if __name__ == "__main__":
    main()
