s="iam studying in AU"
res=" "
word=" "
for char in s:
    if char!=" ":
        word+=char
    else:
            res=word+" "+res
            word=" "
            res=word+ " "+res
