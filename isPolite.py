def isPolite(n):
    ans=[]
    stack=[]
    for numbers in range(1,n):
        for nums in range(numbers,n):
            stack.append(nums)
            if sum(stack)>n:
                stack=[]
                break                   
            elif sum(stack)==n:
                ans.append(stack)
                stack=[]
                break
    print('Politeness of {} is {}'.format(n,len(ans)))
        