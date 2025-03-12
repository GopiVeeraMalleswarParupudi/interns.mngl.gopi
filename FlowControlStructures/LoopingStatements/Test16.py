s='python'
i=0
while(i<len(s)):
    if(s[i]=="h" or s[i]=="p"):
        i+=1
        continue
    else:
        print(s[i]+"\t")
    i+=1