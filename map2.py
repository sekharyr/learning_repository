def camelcaseconvertion(l)
    for i in l:
        i[1].upper()
    return i


 l="my name is john"
i= map(camelcaseconvertion,l)
s=i.join("")