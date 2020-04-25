def isValidSudoku(board) -> bool:
    n=len(board)
    m=len(board[0])
    #check row
    for i in range(n):
        numlist1=[num for num in board[i] if num.isnumeric()]
        if len(set(numlist1))!=len(numlist1):
            return False
       
    #check column
    for k in range(m):
        numlist2=[]
        for l in range(n):
            if board[l][k].isnumeric():
                numlist2.append(board[l][k])
        if len(set(numlist2))!=len(numlist2):
            return False
       
    #check 3x3
    for k in range(0,m,3):
        numlist3=[]
        for l in range(0,n,3):
            numlist3.extend(board[l][k:k+3])
            numlist3.extend(board[l+1][k:k+3])
            numlist3.extend(board[l+2][k:k+3])
            numlist3=[num for num in numlist3 if num.isnumeric()]    
            if len(set(numlist3))!=len(numlist3):
                return False
            numlist3.clear()
  
    return True