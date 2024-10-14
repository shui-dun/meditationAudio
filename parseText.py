import re

def parseText():
    ans = []
    # 从content.md中读取内容
    with open('content.md', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            # 如果line以>开头，则跳过
            if re.match(r'^>', line):
                continue
            # 如果line以#开头，那么就是标题
            isTitle = re.match(r'^#', line)
            # 将[xxx](yyy)转化为xxx
            line = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', line)
            # 删除前导的#号、>号、空格、-号、*号、数字、点号
            line = re.sub(r'^[#>\s\-*\d.]+', '', line)
            # 删除所有的*
            line = re.sub(r'\*', '', line)
            if len(line) > 0:
                ans.append((line, 0 if isTitle else 5))
    print(ans)
    return ans

if __name__ == '__main__':
    ans = parseText()
    print(len(ans))