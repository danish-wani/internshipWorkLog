if __name__ == '__main__':
    n = int(input())
    if n >= 2 and n <= 5:
        global students
        global secondLowestGrade
        secondLowestGrade = []
        students = []
        for _ in range(n):
            name = input()
            score = float(input())
            students.append([name,score])
            students.sort(key = lambda x: x[1])
        min = students[0][1]

        for x in students:
            if x[1] != min:
                second = x[1]
                break

        for y in students:
            if y[1] == second:
                secondLowestGrade.append(y)

        secondLowestGrade.sort(key = lambda x : x[0])
        for s in secondLowestGrade:
            print(s[0])
