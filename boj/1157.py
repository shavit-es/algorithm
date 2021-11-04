def alphabetcount(word):
    countdict ={}
    maxcount=0
    maxkey=""
    duplication=0
    word = word.upper()
    wordlist=list(word)
    for i in range(len(wordlist)):
        countdict[wordlist[i]]=countdict.get(wordlist[i],0)+1
    for key, value in countdict.items():
        if value>maxcount:
            maxkey=key
            maxcount=value
            duplication=0
        elif value==maxcount:
            duplication=1
    if duplication==1:
        print("?")
    else:
        print(maxkey)

w=input()
alphabetcount(w)
