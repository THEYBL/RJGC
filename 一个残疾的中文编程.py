#!/usr/bin/env python
# coding: utf-8

# 使用说明：
# 这是中文编程
# 但是因为时间原因并不完善
# 建议使用时符号仍然使用原来的符号，如：+ - * / =
# 另外一些语句也请仍然使用英文，如：if else

# In[1]:


整型 = int
打印 = print
零 = 0
一 = 1
二 = 2
三 = 3
四 = 4
五 = 5
六 = 6
七 = 7
八 = 8
九 = 9
十 = 10


# In[3]:


num=['零','一','二','三','四','五','六','七','八','九']
 
k=['零','十','百','千','万','十','百']
import time
 
def rankid():
    rank=[]
    for i in range(101):
        a=tstr(i)
        rank.append(a)
    return rank
 
#取整取余并连接，返回连接好的字符串和余数
def turn(x,y):
    if y>= 1:
        a=x//pow(10,y)
        b=x%pow(10,y)
        c=num[a]+k[y]
        if y>4 and b<pow(10,4):
            c+=k[4]
        if (len(str(x))-len(str(b))) >= 2 and b != 0:
            c+=k[0]
    else:
        a=x
        b=0
        c=num[a]
 
    return (c,b,)
#调用上一个函数，以保证进行完所有的数并返回
def 看看(x):
    c=turn(x,(len(str(x))-1))
    a=c[0]
    b=c[1]
    while b != 0:
        a+=turn(b,(len(str(b))-1))[0]
        b=turn(b,(len(str(b))-1))[1]
 
    return a
 


start=time.time()
 
ranki=rankid()
print(ranki)
tstr(12)
end=time.time()-start
print('程序共用时:%0.2f'%end)


# In[ ]:





# 请运行上面之后再尝试中文编程，如：

# In[14]:


气温 = 十
气温=气温 - 三
气温=气温 + 二
打印(看看(气温))
if 气温 > 八:
    打印("你好，世界")
else:
    打印("冻死我了")


# In[13]:


小杨年龄 = 八
小杨零花钱 = 二
小杨年龄 = 小杨年龄 + 一
if 小杨年龄 > 八:
    小杨零花钱 = 小杨零花钱 +1
打印(看看(小杨零花钱))


# In[ ]:




