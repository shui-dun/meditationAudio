import re

def parseText():
    ans = []
    # 从content.md中读取内容
    with open('content.md', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            # 如果line以*或者-或者数字开头，则认为是列表项
            isList = re.match(r'^[\-*\d.]+', line)
            # 将[xxx](yyy)转化为xxx
            line = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', line)
            # 删除前导的#号、>号、空格、-号、*号、数字、点号
            line = re.sub(r'^[#>\s\-*\d.]+', '', line)
            # 删除所有的*
            line = re.sub(r'\*', '', line)
            if len(line) > 0:
                ans.append((line, 6 if isList else 0, False))
    print(ans)
    return ans

if __name__ == '__main__':
    parseText()