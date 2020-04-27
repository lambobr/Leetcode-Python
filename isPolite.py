def isPolite(n):
    ans=[]
    stack=[]
    m=round(n/2)+1
    for numbers in range(1,m): 
        for nums in range(numbers,m):
            stack.append(nums)
            if sum(stack)>n:
                stack=[]
                break                   
            elif sum(stack)==n:
                ans.append(stack)
                stack=[]
                break
    print('Politeness of {} is {}'.format(n,len(ans)))
        
