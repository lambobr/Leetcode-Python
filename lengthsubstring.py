"""Find the length of longest substring without repitition"""

def lengthOfLongestSubstring(s: str) -> int:
        if not s:
            return 0
        
        stack=''
        length=[]
        for i in range(len(s)):
            
            if s[i] in stack:
                length.append(len(stack))
                j=stack.index(s[i])
                stack=stack[j+1:]+s[i]
                
            else:
                stack+=s[i]
                length.append(len(stack))
        
        return max(length)