# https://www.hackerrank.com/challenges/alternating-characters/problem?isFullScreen=true

def alternatingCharacters(s):
    # Write your code here
    stack=[]
    c=0
    for i in s:
        if stack and stack[-1]==i:
            c+=1
        else:
            stack.append(i)
    return c