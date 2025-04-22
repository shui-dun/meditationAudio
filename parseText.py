import re

# 返回处理后的line，以及是否是标题
def parseLine(line):
    line = line.strip()
    # 如果line以>开头，则跳过
    if re.match(r'^>', line):
        return "", False
    # 如果line以#开头，那么就是标题
    isTitle = re.match(r'^#', line)
    isTitle = bool(isTitle)
    # 删除前导的#号、>号、空格、-号、*号、数字、点号
    line = re.sub(r'^[#>\s\-*\d.]+', '', line)
    # 将[xxx](yyy)转化为xxx
    line = re.sub(r'\[([^\[\]]*?)\]\([^\(\)]*?\)', r'\1', line)
    # 将[[xxx|yyy]]转化为yyy
    line = re.sub(r'\[\[([^\[\]]*?)\|([^\[\]]*?)\]\]', r'\2', line)
    # 将[[xxx]]转化为xxx，注意这要在[[xxx|yyy]]之后
    line = re.sub(r'\[\[([^\[\]]*?)\]\]', r'\1', line)
    # 去掉 ^addf3 这种块标识
    line = re.sub(r'\s*\^\w+\s*', '', line)
    # 去掉==
    line = re.sub(r'==', '', line)
    # 去掉~~
    line = re.sub(r'~~', '', line)
    # 删除所有的*
    line = re.sub(r'\*', '', line)
    return line, isTitle

def parseText(simple):
    ans = []
    # 从content.md中读取内容
    with open('content.md', 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith('---'): # simple模式下，只读取---之前的内容
                if simple:
                    break
                else:
                    continue
            line, isTitle = parseLine(line)
            if len(line) > 0:
                ans.append((line, isTitle))
    ans.append(('完成冥想', True))
    print(ans)
    return ans

# 单测
if __name__ == '__main__':
    text = '## 正常**粗体**[[内容]] ^2a335 [[链接|内容]][内容](链接)==高亮==~~删除~~'
    print(parseLine(text))