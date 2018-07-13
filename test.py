
'''
类方法
静态方法
'''
# class Dog:
#     count = 0
#     def __init__(self, name, age, color):
#         self.setName(name)
#         self.setAge(age)
#         self.color = color
#
#
#     # 设置名称
#     def setName(self, name):
#         if len(name) < 2 or len(name) > 4:
#             print("狗狗的名字是非法的")
#             self.__name = ""
#         else:
#             self.__name = name
#
#     # 获取名称
#     def getName(self):
#         return self.__name
#
#     # 设置年龄属性值
#     def setAge(self, age):
#         self.__age = age
#
#     # 得到年龄
#     def getAge(self):
#         return self.__age
#
#
#
#     @staticmethod  # 静态方法
#     def staticMe():
#         print("**************************")
#
#
#     @classmethod  # 类方法
#     def classMethod(cls):
#         cls.count = 999
#
#     '''
#     普通方法
#     a函数中改变
#     b函数中输出
#     '''
#     def a(s):
#         s.count = 100
#
#     def b(self):
#         print("我是在a方法中改变后的值：%d"%self.count)
#
#
# d = Dog('花花',2,"白色")
# # d.setName('小芳斤斤计较军')  #重新设定名称#
# print(d.getName())
# #调用类方法
# d.classMethod()
# #调用普通方法
# d.a()
# d.b()
# print("我是在类方法中改变后的值：%d"%Dog.count)
#
#
# '''
# 静态方法的使用就是不需要创建对象，直接用类名点方法名，加载程序的时候首先加载静态程序，
# 执行顺序是你指定的，加载顺序是电脑指定的，多以不要纠结首先加载它为什么是最后输出
# '''
# Dog.staticMe()



'''
关于日历的模块
# lambda x: x*2, list
'''
# import calendar
#
# print(calendar.calendar(2018,w = 2, l = 1, c = 6))#日历
#
# print(calendar.isleap(2017))#判断是否为闰年
#
# print(calendar.leapdays(2000,2018))#统计从那年到哪年之间有多少个闰年，有头无尾
#
# print(calendar.monthrange(2018,6))#某年某月有多少天
#
# print (calendar.timegm((2018, 7, 5, 10, 13, 55 ))) #获取时间对应的时间戳

'''
高阶函数
map  需求一:将列表中元素转化为 字符串格式的列表
     需求二：将列表中的值的开方后存入新的列表

reduce  相邻元素间运算

filter  过滤
'''

# import functools
#
# #第一种：
# lt = [1,2,3,4,5]
# a1 = list(map(str,lt))
# #第二种  通过lambda表达式  lambda后紧跟变量，冒号后边为 表达式，最后的为实际数据
# a2 = list(map(lambda x: str(x), lt))
#
# #第三种  通过定义函数的方式
# def int2str(num):
#     return str(num)
# a3 = list(map(int2str, lt))
# print(a1)
# print(a2)
# print(a3)
#
# #第一种
# b1 = list(map(lambda x: x ** 2, lt))
# #第二种：没有现成的方法，所以通过定义函数的方式
# def kf(num):
#     return num ** 2
# b2 = list(map(kf, lt))
# print(b1)
# print(b2)
#
# '''
# reduce: 将相邻的两个变量进行运算，将结果返回，在与第三个元素进行运算
#         需求：计算列表中和
# '''
# count = functools.reduce(lambda x,y: x+y,lt)
# print("reduce计算列表中的和：%d"%count)
#
#
# '''
# filter：过滤元素
#         需求：将奇数过滤掉，求偶数的和
# '''
# num = list(filter(lambda x: x%2 == 0, lt))
# count2 = functools.reduce(lambda x,y: x + y, num)
# print("reduce + filter计算列表中偶数的和%d"%count2)
#
# '''
# 两个列表中对应位置处数字相加
# '''
# l1 = [1,2,3,4,5]
# l2 = [2,3,4,5,6]
#
# l3 = list(map(lambda x,y: x + y, l1,l2))
# print("lambda计算两个列表中对应位置处数字的和：%d"%l3)


'''
正则表达式
参数一：匹配规则
参数二：要匹配的字符窜
参数三：flags = re.I  不区分大小写    re.M：匹配多行
match：从头开始匹配  常用5个函数：group（）：匹配到的字符窜
                    groups：返回元祖，其中封装了所有的子组对象
                    start：匹配到的起始位置
                    end：匹配到的结束位置
                    spa：返回匹配到的开始下标 - 结束下标（由头无尾）
                    
search：匹配第一次与规则相同的字符，之后再有相同的不做匹配

findall：以列表的形式返回所有匹配到的字符窜


正则表达式中匹配单个元字符：   0-9表达方式：1、[0123456789] ---> [0-9] --->\d
                            0-9之外的任意字符：\D
                            小写a-z：[a-z]
                            大写A-Z：[A-Z]
                            \w：表示这一位中可能包含的内容范围：a-z、A-Z、0-9、_
                            \W：除了a-z、A-Z、0-9、_之外的任意字符
                            . ：匹配除了换行符以外的所有字符

匹配锚字符：      ^：字符窜的开始符，多行匹配时对每一行匹配
                 $：字符窜的结尾符，多行匹配时对每一行匹配
                 \A：字符窜的开始符，多行匹配时只对第一行匹配
                 \Z：字符窜的结尾符，多行匹配时只对第一行匹配
                 \b：匹配一个字符窜的边界，可以为左边界也可以是右边界
                 \B：匹配除了首尾的内容，只匹配中间的内容

匹配多个数字或者多个英文字母：     模糊匹配(贪婪匹配，满足条件的情况下，尽可能多的匹配数据内容)
                                         x?：标识0-1个  取值范围[0,1]
                                         x+：表示1-无穷多 取值范围[1,无穷多]
                                         x*：表示0-无穷多  取值范围[0,无穷多]
                                
                                
                                取消贪婪行为：标识后边加？（x??,x+?,x*?）
                                
                                
                                精确匹配：
                                x{m}：表示出现m次
                                x{m,}：表示至少m次，上不封顶
                                x{m,n}：表示至少m次，最多n次
                                
正则中分组：  （）     起别名：?P<>

正则中替换：  sub(pattern,repl,string,[count])：  返回字符窜
             subn                           ：返回元祖
             
             参数一：正则规则
             参数二：被替换成的内容
             参数三：需要被替换的字符窜
             参数四：被替换的次数，默认全部替换
             

正则中切割：   split(pattern,string)
              参数一：正则规则
              参数二：需要被切割的字符窜
                    

'''
import re

# print(re.match(r"www","www.baidu.com"))
# print(re.match(r"www","Www.baidu.com",flags=re.I))
# print(re.match(r"www","Www.baidu.com",flags=re.I).group())
# print(re.match(r"www","www.baidu.com",flags=re.I).groups())
# print(re.match(r"www","wwwsss.baidu.com",flags=re.M).groups())
# print(re.match(r"www","Www.baidu.com",flags=re.I).start())
# print(re.match(r"www","Www.baidu.com",flags=re.I).end())
# print(re.match(r"www","Www.baidu.com",flags=re.I).span())

# # match第二种使用方法
# pat1 = re.compile(r"www",flags=re.I)
# print(pat1.match("wWw.baidu.com").group())
#
# #search的两种用法
# str = "hhhwww.baidu.wwwcom"
# print(re.search(r'www',str))
#
# pat2 = re.compile(r'www',flags=re.I)
# print(pat2.search(str))
#
# #findall的用法
# print(re.findall(r'www',str,flags=re.I))

#需求：以laoguo与man进行提取
str1 = 'laoguo is a  good man  laoguo is     a nice man laoguo is a     cool man'
# print(re.findall(r'^laoguo.*man',str1,flags=re.I))#贪婪匹配
# print(re.findall(r'^laoguo.*?man',str1,flags=re.I))#非贪婪匹配


'''
判断qq号码是否合法
1、长度在5-12位之间
2、开头不能为0
3、都是数字类型
'''
# qq = '123s4567'
# pat = re.compile(r'^[1-9]\d{4,11}$')
# mat = pat.search(qq)
# if mat:
#     print("合法，号码为：" + qq)
# else:
#     print("不合法...")

'''
sub替换
'''
# regex = r'laoguo'
# print(re.sub(regex,'老王',str1))


'''
split切割
'''
print(re.split(r' +',str1))  #具有贪婪行为切割
print(re.split(r' +?',str1))  #不具有贪婪行为切割