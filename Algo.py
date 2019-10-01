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

    arrayx = [[0] for y in range(n)]

    for i in range(n):
            while True:
                k = int(input("Enter the number of pairs: "))
                if 1 > k or k > 10:
                    print("Value should be in 1-10")
                    continue
                break

            arrayx[i][0] = k
            for j in range(k):
                s = int(input("Enter the size of program " + str(i+1) + ": "))
                t = int(input("Enter the time of program " + str(i+1) + ": "))
                arrayx[i].append(s)
                arrayx[i].append(t)

            if k == 1:
                min_time1 = arrayx[0][2]
            else:
                min_time1 = arrayx[0][2]
                for i in range(k):
                    if min_time1 > arrayx[0][(i+1)*2]:
                        min_time1 = arrayx[0][(i+1)*2]






    # print(arrayx[0][1])
    # print(arrsize[1])
    print(min_time1)
    # print(list.index(min_time1))




main()