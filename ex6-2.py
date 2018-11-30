def testReEle(lis):
    tem = set(lis)
    if len(tem)==len(lis):
        print (True)
    else:
        print ('False')
def getList():
    lis=[]
    ch=input("请输入判定元素，回车表示结束")
    while ch !='':
        lis.append(ch)
        ch=input("请输入判定元素，回车表示结束:")
    testReEle(lis)
getList()
