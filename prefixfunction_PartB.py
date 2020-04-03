def prefixfunc(pat): 
    m=len(pat)
    pref=[0]*m
    l = 0 
    i = 1
    while i < m: 
        if pat[i]== pat[l]: 
            l=l+ 1
            pref[i] = l
            i =i+ 1
        else: 
            if l != 0: 
                l = pref[l-1] 
            else: 
                pref[i] = 0
                i += 1
    return pref

pat = "aabaabcab"
pref=prefixfunc(pat)
print(pref)
