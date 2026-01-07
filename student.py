import sys

def main():
    name = sys.argv[1]
    m1 = int(sys.argv[2])
    m2 = int(sys.argv[3])
    m3 = int(sys.argv[4])

    total = m1 + m2 + m3
    avg = total / 3

    print("Name:", name)
    print("Marks:", m1, m2, m3)
    print("Total:", total)
    print("Average:", avg)

if __name__ == "__main__":
    main()
