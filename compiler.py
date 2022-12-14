code = "'h1; hi','html;hi'"
code = code.replace(' ','')
code = '['+code+']'
code = eval(code)
print(code)
htmlString = ''
for i in range(len(code)):
    data = code[i]
    frd = ''
    bcd = ''
    found = True
    for _ in range(len(data)):
        if data[_] == ';':
            found = False
        if found:
            frd += data[_]
        else:
            if not data[_] == ';':
                bcd += data[_]

    htmlString += '<'+frd+'>'
    htmlString += bcd
    htmlString += '</'+frd+'>'
    print('et: '+str(i)+' --> frd: '+frd+', bcd: '+bcd)
    print(htmlString)

