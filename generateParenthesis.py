"""This function is used to generate all combinations of n pairs of valid parenthesis""" 
def generateParenthesis(n: int) -> str:
    if n==0:
        return [""]
    
    ans=[]
    pattern=['(']
    
    #The loop runs until all pattern is pushed to ans
    while pattern: 
        new_pattern=[]
        for p in pattern:
            if p.count('(')<n and p.count(')')<p.count('('):
                new_pattern.append(p+'(')
                new_pattern.append(p+')')
            elif p.count('(')<n and p.count(')')==p.count('('):
                new_pattern.append(p+'(')
            elif p.count('(')==n and p.count(')')<p.count('('):
                new_pattern.append(p+')')
            else:
                ans.append(p)
        pattern=new_pattern
        
    return ans