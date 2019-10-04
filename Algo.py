def main():

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

    arrayx = [[] for y in range(n)]
    dupli_arrayx = [[0 for q in range(2)] for y in range(n)]
    for i in range(n):
            while True:
                k = int(input("Enter the number of pairs: "))
                if 1 > k or k > 10:
                    print("Value should be in 1-10")
                    continue
                break

            if k > 1:
                arraytemp = [[] for y in range(k)]
                for j in range(k):
                    s = int(input("Enter the size of program " + str(i + 1) + ": "))
                    t = int(input("Enter the time of program " + str(i + 1) + ": "))
                    arraytemp[j].append(s)
                    arraytemp[j].append(t)

                def takeSecond(elem):
                    return elem[1]

                arraytemp.sort(key=takeSecond)
                arrayx[i] = arraytemp[0]
                del arraytemp[:]

            elif k == 1:
                for j in range(k):
                    s = int(input("Enter the size of program " + str(i + 1) + ": "))
                    t = int(input("Enter the time of program " + str(i + 1) + ": "))
                    arrayx[i].append(s)
                    arrayx[i].append(t)

    for i in range(n):
        for j in range(2):
            dupli_arrayx[i][j] = arrayx[i][j]

    def takeSecond(elem):
        return elem[1]

    dupli_arrayx.sort(key=takeSecond)
    print(dupli_arrayx)

    print("second", arrayx)


main()