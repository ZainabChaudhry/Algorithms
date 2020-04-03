def bmp(t, p): 
    dummy=256 # while working with alphabets it is preffered to make in 256  
             #or asci vaue of the maximum character can also be used
    m = len(p) 
    n = len(t) 
    bc = [0]*dummy
    k = 0
    z=0
    for i in range(m): 
        bc[ord(p[i])] = i;  # reprsesents badcharacter array the mismatched one
    while(k <= n-m): 
        j = m-1
        while j>=0 and p[j] == t[k+j]: 
            j -= 1
        if j<0: 
            print("Pattern occur at shift " ,k) 
            z=1
            if(k+m<n):
                k += m-bc[ord(t[k+m])]
            else:
                k+=1
        else: 
            k += max(1, j-bc[ord(t[k+j])])
    if(z==0):
        print("notfound")
text = "earning"
pattern = "ing"
bmp(text, pattern)
