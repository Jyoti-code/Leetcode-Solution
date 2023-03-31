# https://www.hackerrank.com/challenges/reduced-string/problem?isFullScreen=false

def superReducedString(s):
    # Write your code here
        x=[]
        for i in s:
            if len(x)>0 and x[-1]==i:
                x.pop()
            else:
                x.append(i)
        if len(x)==0:
            return "Empty String"
        else:
            return ''.join(x)