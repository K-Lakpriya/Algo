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
    time = []
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
                # print(time)

            if k == 1:
                min_time1 = arrayx[i][2]
                d_size = arrayx[i][1]
                time.append(t)
            else:
                min_time1 = arrayx[i][2]
                d_size = arrayx[i][1]
                for q in range(k):
                    if min_time1 >= arrayx[i][(q+1)*2]:
                        min_time1 = arrayx[i][(q+1)*2]
                        d_size = arrayx[i][(q+1)*2-1]
                        # for poped in range(k):
                # time.pop()
                time.append(min_time1)
            print(min_time1)
            print(d_size)

            for z in range(len(time)):
                cursor = time[z]
                pos = z

                while pos > 0 and time[pos - 1] > cursor:
                    # Swap the number down the list
                    time[pos] = time[pos - 1]
                    pos = pos - 1
                # Break and do the final swap
                time[pos] = cursor

    print(time)


main()