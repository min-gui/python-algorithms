

def stack_sequence(n, sequence):

    num = 1
    stack = []
    answer = []
    for i in sequence:

        while(num <= i):
            stack.append(num)
            answer.append("+")
            num += 1

        if stack and stack[-1] == i:
            stack.pop()
            answer.append("-")
        else:
            print("NO")
            break

    if not stack:
        for i in answer:
            print(i)

sequence = list()
n = int(input())
for _ in range(n):
    sequence.append(int(input()))
stack_sequence(n, sequence)