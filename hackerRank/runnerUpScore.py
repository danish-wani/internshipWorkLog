if __name__ == '__main__':
    n = int(input())
    if n >= 2 and n <= 10:
        arr = list(map(int, input().split()))
        lis=[1,2,3]   
        arr.sort()
        maxScore = max(arr)
        print(arr[arr.index(maxScore)-1])
