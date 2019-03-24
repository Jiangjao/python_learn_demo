#对那些标记的输出的开始和结束提供了一个友好的访问接口

class Handler:
    """
    处理程序父类，处理常见的HTML标签，如标题(title)，列表(list)等，主要实现方法在其子类中
    """
    #定义回调函数，调用该类中函数名为prefix + name的方法，输入参数为*args
    def callback(self, prefix, name, *args):
        #getattr获取对象属性self.(prefix+name) 或者none
        method = getattr(self, prefix + name, None)
        # return true 不一定可调用；return false 一定不可调用
        #如果调用(callable),则返回 方法
        if callable(method): return method(*args)

    def start(self, name):
        self.callback('start_', name)

    def end(self, name):
        self.callback('end_', name)

    def sub(self, name):
        #定义substitution函数，该函数将作为 re.sub 函数的第二个参数
        #该函数的作用是替换制定规则的字符串，例如正则表达式
        def substitution(match):
            #只要进入这个函数，就表示有匹配的字符串
            #若callback返回的字符串为空，则返回采用完整的匹配
            #否则返回回调函数中的字符串
            result = self.callback('sub_', name, match)
            if result is None: result = match.group(0) #group(0)表示完整的匹配
            return result

        return substitution

#提供那些固定的HTML标记的输出（每一个标记都有start和end)
class HTMLRenderer(Handler):
    """
    docstring for HTML,get HTML marker to block
    Handler类的子类，给文本块添加相应的HTML标签
    """
    # def __init__(self, arg):
    # 	super(HTML, self).__init__()
    # 	self.arg = arg

    def start_document(self):
        print('<html><head><title>ShiYanLou</title></head><body>')

    def start_paragraph(self):
        print('<p style="color:#444;">')

    def end_paragraph(self):
        print('</p>')

    def start_heading(self):
        print('<h2 style="color:#68BE5D;">')

    def end_heading(self):
        print('</h2>')

    def start_list(self):
        print('<ul style="color: #363736;">') #<ul>标签定义无序列表

    def end_list(self):
        print('</ul>')

    def start_listitem(self): #<li>标签定义无序列表中的每一项
        print('<li>')

    def end_listitem(self):
        print('</li>')

    def start_title(self):
        print('<h1 style="color: #1ABC9C;">')

    def end_title(self):
        print('</h1>')

    #定义过滤器的回调函数（以下三个）
    def sub_emphasis(self, match):
        return ('<em>%s</em>' % match.group(1)) #匹配字符串转换成html强调字符

    def sub_url(self, match):
        return ('<a target="_blank" style="text-decoration:none;color:#BC1A4B;" href="%s">%s</a>'
                    % (match.group(1), match.group(1))) #group(1)表示匹配子组1

    def sub_mail(self, match):
        #之所以用子组1是添加过滤器时设置了子组
        return ('<a target="_blank" style="text-decoration:none;color:#BC1A4B;" href="mailto:%s">%s</a>'
                    % (match.group(1), match.group(1)))

    def feed(self, data):
        print(data)
"""这个程序勘称是整个"项目"的基础：提供标签的输出，以及字符串的替换"""
