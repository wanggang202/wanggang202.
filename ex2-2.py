TempStr=input("请输入带有符号的金钱数额:")
if TempStr[-1]in['D','d']:
    Y = 6*eval(TempStr[0:-1])
    print("转换后的钱数是{:.2f}Y".format(Y))
elif TempStr[-1]in['Y','y']:
        D=eval(TempStr[0:-1])/6
        print("转换后的钱数是{:.2f}D",format(D))
else:
    print("输入错误")
