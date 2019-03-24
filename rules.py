#Rule类来判断每个文本块交给处理程序将要添加什么标记
"""
这个模块，其他拥有它的俩个方法是condition和action,
condition:判断字符串是否符合规则
action:   执行操作,即调用"处理程序模块",输出带标签的内容...

"""
class Rule:
    """
    规则父类,处理字符串的规则，
    首先添加标签的起始标记，然后处理字符串，最后添加标签结束标记
    """
    def action(self, block, handler):
        """
        加标记
        """
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        return True #action函数返回bool值的原因：执行当前操作之后还有可能
#要执行其他的action函数
"""
如listItemRule类的action函数返回后还可以执行ListRule类的action函数
所以需要bool值的原因可以解释为：表示是否应该停止处理当前块的规则
"""
                    


class HeadingRule(Rule):
    """
    一号标题规则
    """
    type = 'heading'

    def condition(self, block):
        """
        判断文本块是否符合规则
        string中没有换行符，且string的长度小于等于70，且字符串最后一个字符不等于':'
        """
        return not '\n' in block and len(block) <= 70 and not block[-1] == ':'
        #如果没有重写action函数，则表明是继承父类的action函数

class TitleRule(HeadingRule):
    """
    二号标题规则
    """
    type = 'title'
    first = True

    def condition(self, block):
        if not self.first:
            return False
        self.first = False
        return HeadingRule.condition(self, block)


class ListItemRule(Rule):
    """
    列表项规则
    """
    type = 'listitem'

    def condition(self, block):
        return block[0] == '-'

    def action(self, block, handler):
        handler.start(self.type)
        handler.feed(block[1:].strip()) #忽略第一个字符'-',并删除空格
        handler.end(self.type)
        return True


class ListRule(ListItemRule):
    """
    列表规则
    """
    type = 'list'
    inside = False

    def condition(self, block):
        return True

    def action(self, block, handler):
        if not self.inside and ListItemRule.condition(self, block):
            handler.start(self.type)
            self.inside = True
        elif self.inside and not ListItemRule.condition(self, block):
            handler.end(self.type)
            self.inside = False
        return False
        '''这个有一个bug，当以列表结束的时候，会导致m后面少了一个</ul>'''


class ParagraphRule(Rule):
    """
    断落规则
    """
    type = 'paragraph'

    def condition(self, block):
        return True
