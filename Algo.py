def main() :

    while True:
            m = int(input("Enter the number of memory partitions: "))
            if 0 > m or m > 10:
                print("Value should be in 1-10")
                continue

            n = int(input("Enter the number of programs: "))
            if 0 > n or n > 50:
                print("Value should be in 1-50")
                continue

            if n == 0 or m == 0:
                print("program will exit")
                exit()
            break

    arrsize = []

    for i in range(m):
        size = int(input("Enter the size of the memory partition " + str(i+1) + ":"))
        arrsize.append(size)

    while True:
        for i in range(n):
            k = int(input("Enter the number of pairs: "))
            if 0 > k or k > 10:
                print("Value should be in 1-10")
                continue
            for x in range(k):
                arrx = [[]]
                s = int(input("Enter the size of " + str(i+1) + "program: "))
                arrx.append(s)
                t = int(input("Enter the time of " + str(i+1) + "program"))
                arrx.append(t)








main()