def main():

    case = 0
    avarage_time = []
    Dict = {}

    # getting inputs and checking the inputs are in range
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
                exit()  #Exit from the function if enter 0 0
            break

    arrsize = [] #to store size of the memory partition

    for i in range(m):
        size = int(input("Enter the size of the memory partition " + str(i+1) + ":"))
        arrsize.append(size)    #store memory sizes

    #lists for store test values
    arrayx = [[] for y in range(n)]
    dupli_arrayx = [[0 for q in range(3)] for y in range(n)]

    #getting inputs of program size and time
    for i in range(n):
            while True:
                k = int(input("Enter the number of pairs: "))
                if 1 > k or k > 10:
                    print("Value should be in 1-10")
                    continue
                break

            #choosing minimum time program if there is more than 1 sub programs
            if k > 1:
                arraytemp = [[] for y in range(k)]
                for j in range(k):
                    s = int(input("Enter the size of program " + str(i + 1) + ": "))
                    t = int(input("Enter the time of program " + str(i + 1) + ": "))
                    arraytemp[j].append(i+1)
                    arraytemp[j].append(s)
                    arraytemp[j].append(t)

                def takeSecond(elem):
                    return elem[2]

                arraytemp.sort(key=takeSecond)
                arrayx[i] = arraytemp[0]
                del arraytemp[:]

            elif k == 1:
                for j in range(k):
                    s = int(input("Enter the size of program " + str(i + 1) + ": "))
                    t = int(input("Enter the time of program " + str(i + 1) + ": "))
                    arrayx[i].append(i+1)
                    arrayx[i].append(s)
                    arrayx[i].append(t)

    #sorting the list in ascending order
    for i in range(n):
        for j in range(3):
            dupli_arrayx[i][j] = arrayx[i][j]

    def takeSecond(elem):
        return elem[1]

    dupli_arrayx.sort(key=takeSecond)


    # getting avarage time and enter programs into nessassory regions
    time_memory = [0] * m
    turn = -1
    for_print = []

    for i in range(n):
            while(1):
                turn = (turn+1) % m

                if dupli_arrayx[i][1] <= arrsize[turn]:
                    start_time = time_memory[turn]
                    end_time = time_memory[turn] + dupli_arrayx[i][2]
                    time_memory[turn] = time_memory[turn] + end_time
                    for_print.append([turn, dupli_arrayx[i][0], start_time, end_time])

                    break

    avarage_time.append(sum(time_memory) / n)

    #sorting values to print
    sorting_for_print = sorted(for_print, key=lambda time: time[1])
    Dict.update({case: sorting_for_print})


    #printing the values
    for final, amnt in Dict.items():
        print(f'Case {final + 1}')
        print(f'Average Turnaround time {avarage_time[final]:.2f}')
        for p, q in enumerate(amnt, 0):
            print(f'Program {amnt[p][1]} runs in region {amnt[p][0] + 1} from time {amnt[p][2]} to {amnt[p][3]}')


main()