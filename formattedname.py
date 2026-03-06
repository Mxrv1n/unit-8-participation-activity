def formatname(first,second,middle=''):
    if middle:
        fullname=f"{first} {middle} {second}"
    else:
        fullname=f'{first} {second}'
    return fullname.title()
musician = formatname('julian','casablancas','fernando')
print(musician)
musician = formatname('jack','white')
print(musician)