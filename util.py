""""
@description:首先我们需要有一个文本块生成器把纯文本分成一个一个的文本块，
            以便接下来对每一个文本块进行解析，util.py 代码如下
"""
# def lines(file):
#     """
#     生成器，在文本最后加一空行,即换行操作
#     """
#     for line in file:
#         yield line
#     yield '\n'


# def blocks(file):
#     """
#     生成器，生成单独的文本块
#     """
#     block = []
#     for line in lines(file):
#         if line.strip():                   #去掉string的前后端的空格，判断是否为真
#             block.append(line)             #真，将string添加到block中
#         elif block:                        #假，判断block是否空的
#             # strip() 函数可以去除一个字符串前后的空格以及换行符
#             yield ''.join(block).strip()   #不为空，将block中所有的元素连接起来为一个新的string，
#                                            #元素之间的连接字符为空
#             block = []                     #清除缓存，读取后面的内容

# print(blocks(open('test.txt').read()))

from	sys	import	argv
script,	filename	=	argv
txt	=	open(filename)

def lines(file):
    i = 0 
    """
    geneotor to get newline
    yield ： return a genenarotor ,until no element
    """
    for line in file:
        i += 1
        print(line,i)
        
    print('\n',1) 

def blocks(file):
    """
    geneotor to get single letter blocks
    """
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            # strip() 函数可以去除一个字符串前后的空格以及换行符
            yield ''.join(block).strip()
            block = []

# print("Here's	your	file %r:" % filename)	 
# print(txt.read())

print("Here's	your	file txt")	
print(lines(txt))
print("Here's	your	file blocks")	
print(blocks(txt))


	