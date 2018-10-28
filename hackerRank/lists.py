if __name__ == '__main__':
    global data
    data = []
    global commands
    commands = []
    N = int(input())
    for _ in range(N):
        commands.append(input().split())
        
    for c in commands:
        if c[0] == 'insert':
            data.insert(int(c[1]),int(c[2]))
        elif c[0] == 'print':
            print(data)
        elif c[0] == 'remove':
            data.remove(int(c[1]))
        elif c[0] == 'append':
            data.append(int(c[1]))
        elif c[0] == 'sort':
            data.sort()
        elif c[0] == 'pop':
            data.pop()
        elif c[0] == 'reverse':
            data.reverse()

