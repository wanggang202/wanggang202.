from math import*
def isPrime(num):
    try:
        num = eval(num)
        if type(num) == type(1):
            if num == 1:
                return False
            else:
                for i in range(2,int(sqrt(num+1))):
                   if num % i == 0:
                      return False
            return True
    except:
        print("输入有误!请输入整数")
        if_name_=='_main_'
n=input("请输入整数: ")
print(isPrime(n))
