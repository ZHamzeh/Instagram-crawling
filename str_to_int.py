def str_to_int(s):
    number = ''
    flag = False
    lenght = len(s)
    for i in range(lenght):
        if s[i]=='0':
          number+= '0'
        elif s[i]=='1':
          number+= '1'
        elif s[i]=='2':
          number+= '2'
        elif s[i]=='3':
          number+= '3'
        elif s[i]=='4':
          number+= '4'
        elif s[i]=='5':
          number+= '5'
        elif s[i]=='6':
          number+= '6'
        elif s[i]=='7':
          number+= '7'
        elif s[i]=='8':
          number+= '8'
        elif s[i]=='9':
          number+= s[i]
        elif s[i]=='k':
            number+='000'
        elif s[i]=='m':
            number +='000000'
        elif s[i]=='.':
            flag = True
        else:
            pass

    number = int(number)
    if flag == True:
        number = int(number/10)
    return number
