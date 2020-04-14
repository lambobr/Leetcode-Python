
m=int(input('Enter a number to check if it is a happy number or not:'))

def isHappy(n: int) -> str:
    """This function is used to determine if the inputted number is a Happy Number or not"""
    count=0
    m=n
    while count<10:
        s=0
        while n>0:
            z=n%10
            s+=z**2
            n=n//10
        count+=1
        n=s
    if n==1:
        print('The number {} is a happy number.'.format(m))
    else:
        print('The number {} is NOT a happy number.'.format(m))
        
    del m
    
    
    
#Run the function
isHappy(m)
            
            