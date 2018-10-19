#没有出现过无故中断情况下
dayuo, dayfactor, dayupa =1,0.01,1
for i in range(365):
    if i% 11 in[3,4,5,6]:
        dayup=dayuo*(1+dayfactor)
else:
    dayup=dayup
print("10天休息一次:{:.2f}".format(dayup))
for i in range(365):
    if i% 16 in[4,5,6,7,11,12,13,14]:
        dayupa=dayupa*(1+dayfactor)
else:
    dayupa=dayupa
print("15天休息一次:{:.2f}".format(dayupa))
