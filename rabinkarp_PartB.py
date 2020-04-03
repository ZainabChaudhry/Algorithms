def rabinkarp(p, t, q): 
    dummy = 16 # this can be any positive number that is used incalculation of hash value 
          #but is prefered to be equal to the the input characters of text
    n = len(t)
    m = len(p) 
    ph = 0    # hash value for pattern 
    th = 0    # hash value for txt 
    h = 1
    for i in range(m-1): 
        h = (h * dummy)% q 
    k=0
    while(k<m):
        ph = (dummy * ph + ord(p[k]))% q 
        th = (dummy * th + ord(t[k]))% q 
        k+=1
    l=0
    while(l<n-m+1): # sliding pattern 
        if ph == th: 
            for j in range(m): 
                if t[l + j] != p[j]: 
                    break
            j+= 1
            if j == m: 
                print("Pattern found at index " ,l, " and end at ", l+m)
        if l < n-m: 
            th = (dummy*(th-ord(t[l])*h) + ord(t[l + m]))% q 
            if th < 0: 
                th += q
        l+=1

text = "3141592653589793"
pattern = "26"
q = 11 # A prime number 
rabinkarp(pattern, text, q) 
