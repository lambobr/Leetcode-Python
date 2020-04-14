"""Convert romal numeral (str) to numbers (int)"""

def romanToInt(s: str) -> int:
    romans=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    numerals=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    output=0
    for i in range(len(romans)):
        while romans[i]==s[:len(romans[i])]:
            output+=numerals[i]
            s=s.replace(romans[i],'',1)
            
    return output

