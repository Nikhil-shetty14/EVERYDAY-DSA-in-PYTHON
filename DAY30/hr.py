if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        line = input().split()
        name, marks = line[0], list(map(float, line[1:]))
        student_marks[name] = marks
    query_name = input()
    marks = student_marks[query_name]
    print("{:.2f}".format(sum(marks) / len(marks)))

    """2"""

    if __name__ == '__main__':
    N = int(input())
    lst = []
    for _ in range(N):
        cmd = input().split()
        if cmd[0] == 'insert':
            lst.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == 'print':
            print(lst)
        elif cmd[0] == 'remove':
            lst.remove(int(cmd[1]))
        elif cmd[0] == 'append':
            lst.append(int(cmd[1]))
        elif cmd[0] == 'sort':
            lst.sort()
        elif cmd[0] == 'pop':
            lst.pop()
        elif cmd[0] == 'reverse':
            lst.reverse()