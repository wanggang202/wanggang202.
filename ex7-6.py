def rdic():
    fr = open('dic.txt','r')
    for line in fr:
        line = line.replace("\n",'')
        v = line.split(':')
        dic[v[0]] = v[1]
        keys.append(v[0])
    fr.close()
def centre():
    n = input("请输入相应模块(添加,查询,退出):")
    if n =="添加":
        key = input("请输入英语单词:")
        if key not in keys:
            value = input("请输入英语单词:")
            dic[key] = value
            keys.append(key)
            peint("单词添加成功")
        else:
            print("该单词已经添加至字典库")
    elif n == "查询":
        key = input("请输入英语单词:")
        if key in keys:
            print("中文意思为:"+dic[key])
        else:
            print("字典中为知道这个单词")
    elif n == "退出":
        return 1
    else:
        print("输入有误")
        return 0
def wdic():
    with open('dic.txt','w') as fw:
        for k in keys:
            fw.write(k+':'+dic[k]+'\n')
if __name__=="__main__":
    keys = []
    dic = []
    while True:
        rdic()
        n = centre()
        wdic()
        if n == 0:
            continue
        elif n == 1:
            break
