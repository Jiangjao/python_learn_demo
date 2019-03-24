import re
import sys
'''
e^x的麦克劳林展开式: 
e^x= f（0）+ f′（0）x+ f″（0）x ²/ 2!+...+ fⁿ（0）x^n/n!+Rn(x）
=1+x+x^2/2!+x^3/3!+...+x^n/n!+Rn(x） 
'''

# # 阶乘函数
# def factorial(n):
#     x = 1
#     for i in range(1,n+1):
#         x = x * i
#     return x

# # y值函数
# def consY(n,x):
#     y = 1
#     for i in range(1,n):
#         y += x**i/factorial(i)
#     return y

# # 生成图像
# def moniPlot(n,x):
#     # 定义一个颜色集合
#     colors = ['g','b','black','cyan','lightgreen','yellow','deeppink','darkorchid']
#     plt.figure()
    
#     # 原函数
#     y = np.e**x
#     # 画原函数图像并进行标记
#     plt.plot(x,y,'r-',linewidth=2,label='e^x')
    
#     # 麦克劳林展开添加到图像上
#     for i in range(2,n):
#         y = consY(i,x)
#         # 随机选择颜色
#         color = colors[random.randint(0,len(colors)-1)]
#         linestyle = '--'
#         # 画图像，并对最后一个进行标记
#         if i == n:
#             plt.plot(x,y,color=color,linewidth=1,linestyle=linestyle,label="nearly e^x")
#         else:
#             plt.plot(x,y,color=color,linewidth=1,linestyle=linestyle)
#         plt.plot(x,y,color=color,linewidth=1,linestyle=linestyle)
#     #添加注释
#     plt.text(1.2, consY(10,3.9),"Maclaurin's series of e^x ",size=12)
    
#     # 将标记绘制图例，位置为于中间左侧
#     plt.legend(['e^x',"nearly e^x"], loc = 'center left')  
    
#     plt.show()
import sys , re
from handlers import *
from util import *
from rules import *
# 这个模块的作用就是协调读入的文本和其他模块之间的关系
# 提供了存放'规则'和'过滤器'的列表

class Parser:
    """
    解释器父类
    读取.txt文件，应用rules并且控制handler
    """

    def __init__(self, handler):
        self.handler = handler
        self.rules = []
        self.filters= []
            
    def addRule(self, rule):
        """
        添加规则到规则列表
        """
        self.rules.append(rule)


    def addFilter(self, pattern, name):
        """
        添加过滤器到过滤器列表
        """
        def filter(block, handler): #创建过滤器
            return re.sub(pattern, handler.sub(name), block)
        self.filters.append(filter)

    def parse(self, file):
        """
        解析
        """
        self.handler.start('document')
        for block in blocks(file):
            for filter in self.filters:
                block = filter(block, self.handler)
            #judge_list = True
            for rule in self.rules:
                if rule.condition(block):  #判断字符串属于哪一类规则
                    last = rule.action(block, self.handler) #运行规则处理字符串
            #judge_list = last
                    if last:
                        break
            #if not judge_list: self.handler.end('list')
        self.handler.end('document')


class BasicTextParser(Parser):
    """
    纯文本解析器
    """

    def __init__(self, handler):
        Parser.__init__(self, handler) #调用父类构造函数

        #添加解析规则类
        self.addRule(ListRule())
        self.addRule(ListItemRule())
        self.addRule(TitleRule())
        self.addRule(HeadingRule())
        self.addRule(ParagraphRule()) #最后添加段落规则，应为段落规则condition始终返回true

        #正则表达式
        #括号里表示保存为子组，与HTMLRender中的过滤器函数对应
        self.addFilter(r'\*(.+?)\*', 'emphasis')
        self.addFilter(r'(http://[\.a-zA-Z/]+)', 'url') #url规则可改
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail') #可改


"""
运行程序
"""
handler = HTMLRenderer()          #定义
parser = BasicTextParser(handler) #初始化
parser.parse(sys.stdin)           #解析输入的文件，转换成html文件

'''这个程序的用途: 1、用来做代码高亮分析，如果改写成js版的话，可以做一个在线代码编辑器。
                   2、可以用来学习，供写博文用。 '''
'''运行方式：在cmd或者终端中输入
    python test.py < test_input.txt > test_output.html
    python表示用python.exe 运行test.py
    <表示从<之后的描述符输入，即从test_input.txt输入
    >表示从>之后的描述符输出，即输出到test_output.html'''
