# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 10:01:18 2019

@author: Lenin
"""
import random

liangci = ['一个','两位','十几个','三个','四个','一群','无数','一亿个','无限个']

xingrongci = ['郁郁寡欢的','兴奋的','美丽的','呆萌的','开心的','没头没脑的','无病呻吟的','勇敢的','可爱的']

zhuyu = ['老人','美女','小孩','大叔','高达','怪兽','奥特曼','钢铁侠','剑客','猫','狗']

weiyu = ['站在','躺在','趴在','跪在','伫立于','倚在','盘腿坐在','单膝跪在']

didian = ['大桥下','马桶上','垃圾桶上','书桌上','大树上','床上','天花板上','阳台上','飞机上']

dongzuo = ['读书','打dota','唱戏','跳舞','吃饭','喝水','玩耍','打台球','踢足球','游泳']




#---所有可能的输出--------------------
'''
for i in liangci:
    for j in xingrongci:
        for k in zhuyu:
            for l in weiyu:
                for m in didian:
                    for n in dongzuo:
                
                        print(i+j+k+l+m+n+'\n'+i+j+k+n+l+m+'\n'+l+m+i+j+k+n+'\n'+l+m+n+i+j+k+'\n'+n+i+j+k+l+m+'\n'+n+l+m+i+j+k)

'''
'''
a = liangci[random.randint(0,len(liangci)-1)]+xingrongci[random.randint(0,len(xingrongci)-1)]+zhuyu[random.randint(0,len(zhuyu)-1)]
b = weiyu[random.randint(0,len(weiyu)-1)]+didian[random.randint(0,len(didian)-1)]
c = dongzuo[random.randint(0,len(dongzuo)-1)]
d = [a,b,c]
random.shuffle (d)

#---顺序输出-----------------------------------
#print(a+b+c)


#---随机输出-----------------------------------
print(''.join(d))
'''

#---随机输出n句无重复-----------------------------------
num = 5 #输出几句无重复短句

i = random.sample(liangci, num)
j = random.sample(xingrongci, num)
k = random.sample(zhuyu, num)
l = random.sample(weiyu, num)
m = random.sample(didian, num)
n = random.sample(dongzuo, num)
for ii in range(num):
    a = i[ii]+j[ii]+k[ii]
    b = l[ii]+m[ii]
    c = n[ii]
    d = [a,b,c]
    random.shuffle (d)
    #print(''.join(d))#无序
    print(a+b+c)#有序



