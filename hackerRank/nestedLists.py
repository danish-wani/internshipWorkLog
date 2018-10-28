if __name__ == '__main__':if __name__ == '__main__':

    n = int(input())
    if n >= 2 and n <= 5:
        global students
        students = []
        for _ in range(n):
            name = input()
            score = float(input())
            temp = [name,score]
            students.append(temp)
            students.sort(key = lambda x: x[1])

        if len(students) == 2:
            if students[0][1] != students[1][1]:
                print( students[0][0])
            else:
                students.sort(key = lambda x : x[0])
                print(students)
        elif len(students) == 3:
            print(students[1][0])
        elif len(students) == 4:
            if students[0][1] != students[1][1] and students[1][1] != students[2][1] and students[2][1] != students[3][1]:
                print(students[1][0])
            elif students[0][1] == students[1][1]:
                print(students[2][0])
            elif students[3][1] == students[2][1]:
                print(students[1][0])
            else:
                students.sort(key = lambda x: x[0])
                print(students[1][0])
                print(students[2][0])
        elif len(students) == 5:
            if students[0][1] != students[1][1] and students[1][1] != students[2][1] and students[2][1] != students[3][1] and students[3][1] != students[4][1]:
                print(students[1][0])
            elif students[0][1] == students[1][1] == students[2][1]:
                print(students[2][0])
            elif students[0][1] == students[1][1] and students[1][1] != students[2][1] and students[2][1] != students[3][1]:
                print(students[2][0])
            elif students[0][1] != students[1][1] and students[1][1] == students[2][1] and students[2][1] != students[3][1]:
                students.sort(key = lambda x: x[0])
                print(students[1][0])
                print(students[2][0])
            elif students[0][1] != students[1][1] and students[1][1] == students[2][1] and students[2][1] == students[3][1] and students[3][1] != students[4][1]:
                students.sort(key = lambda x: x[0])
                print(students[1][0])
                print(students[2][0])
                print(students[3][0])

