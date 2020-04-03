def matching(t, p): 
    # t represents text and p represents pattern
    n = len(t)
    m = len(p)  
    i = 0
    while (i <=n-m): 
        for j in range(0,m): 
            if p[j] != t[i+j]: 
                break
            j+=1
        if j==m:
            print("Pattern found at index ",i," and ended at index ",i+m)
            i+=m 
        elif j==0: 
            i+=1
        else: 
            i+=j # this is the place where if pattern not found the next searching starts from i+j 

pattern = "wxyz"
text = "wxyuwxyzutwxhu"
matching(text, pattern) 
