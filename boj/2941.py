w=input()
count=0
while True:
    if 'c=' in w:
        count+=w.count('c=')
        w=w.replace('c=',"/")
    elif 'c-' in w:
        count+=w.count('c-')
        w=w.replace('c-',"/")
    elif 'dz=' in w:
        count+=w.count('dz=')
        w = w.replace('dz=','/')
    elif 'd-' in w:
        count+=w.count('d-')
        w=w.replace('d-',"/")
    elif 'lj' in w:
        count+=w.count('lj')
        w=w.replace('lj',"/")
    elif 'nj' in w:
        count+=w.count('nj')
        w=w.replace('nj',"/")
    elif 's=' in w:
        count+=w.count('s=')
        w=w.replace('s=',"/")
    elif 'z=' in w:
        count+=w.count('z=')
        w=w.replace('z=',"/")
    else:
        count+=len(w.replace("/",""))
        break
print(count)
