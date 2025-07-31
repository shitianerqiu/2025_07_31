""" 
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。

示例 ：
    输入：s = "()[]{}"
    输出：true

 """

def isValid(intervals):
    # 定义一个栈
    stack = []
    # 定义括号的配对关系
    bracket_map = { ')': '(' , '}': '{' , ']': '[' }

    # print('s ', s)
    # 遍历字符串中的每个字符
    for char in s:
        # print('char ', char)
        # 如果是闭括号
        if char in bracket_map:
            # 弹出栈顶元素，如果栈为空，返回一个虚拟字符
            top_element = stack.pop() if stack else '#'
            # print('top_element ', top_element)
            # 如果栈顶元素不匹配，返回False
            if bracket_map[char] != top_element:
                return False
        else:
            # 如果是开括号，压入栈
            stack.append(char)
        
        # print('stack ', stack)
    
    # 如果栈为空，表示所有的括号都匹配了
    return not stack
        

# 示例测试
s = "()[]{}"
print(isValid(s))