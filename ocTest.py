F = open('words.txt','r' )
allWords = F.read()
listAll = allWords.split(" ")
f = open('Q1.txt','w')

word = ''
serial = 0
i = 0
result = []
# 大迴圈a
while i < len(listAll):
    state = 0
    j = 0
    # 小迴圈b
    while i - j > 0:
        if listAll[i] == listAll[i - j - 1]:
            state = 1
            j = i + 1
        elif i == j :
            state = 0
        else:
            j += 1
    if state == 0:
        # 直接輸出確認無誤
            print(listAll[i]+' '+ str(serial)+ ' ' + str(listAll.count(listAll[i])))
        # 把輸出的內容加入文檔中
            f.write( listAll[i]+' '+ str(serial)+ ' ' + str(listAll.count(listAll[i]))+'\n')
            serial += 1
            i += 1
    elif state == 1:
            i += 1



