def is_correct_parenthesis(string):
    i = string[0]
    stack = []
    print(len(string))
    for j in string:
        if len(stack) != 0:
            top = stack[-1]
            if (top != j):
                stack.pop()
            else:
                stack.append(j)
        else:
            stack.append(j)

    if len(stack) == 0:
        return True
    return False


print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))
