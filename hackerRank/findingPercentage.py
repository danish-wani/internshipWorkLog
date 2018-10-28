from decimal import Decimal
if __name__ == '__main__':
    n = int(input())
    if n >= 2 and n <= 10:
        student_marks = {}
        sum = 0.00
        for _ in range(n):
            name, *line = input().split()
            scores = list(map(float, line))
            student_marks[name] = scores
    
        query_name = input()
        for s in student_marks[query_name]:
            sum = (sum + s)
        sum = Decimal(sum)
        print (round((sum/len(student_marks[query_name])),2))
