import os.path
import re
# -*- coding: utf-8 -*-
# code=cp936

folder = os.path.abspath('.')
fileName = 'combi.js'
path = os.path.join(folder, fileName)
print(path)
# exit()
with open(path, 'r+') as f:
    #读取文件
    allCombinationsText = f.read()
    print(allCombinationsText)
    exit('Done')
    #regex匹配找出每个组合后面的注释字符串
    pattern = re.compile(r'\/\/\s[\u4e00-\u9fa5]{2,4}\"\,')
    result = pattern.findall(allCombinationsText)
    #删除所有注释字符串
    for item in result:
        allCombinationsText = allCombinationsText.replace(item,'')
    #现在是干净的文档了，接下来可以删除不需要的了。
    print(allCombinationsText)
    #调整格式
    # allCombinationsText = allCombinationsText.replace('name','"name"').replace('combinationName','"combinationName"').replace('tiaoJian','"tiaoJian"').replace('activateProperty ','"activateProperty" ').replace('activatePropertyVal ','"activatePropertyVal" ').replace('activateHighProperty ', '"activateHighProperty" ').replace('activateHighPropertyVal ','"activateHighPropertyVal" ')
    # f.seek(0)
    # f.truncate()
    # f.write(allCombinationsText)
    #定义变量
    allCombinationsText = allCombinationsText.split('[')[1].split(']')[0]
    exec('allCombinations =' + '[' + allCombinationsText + ']')
    print(type(allCombinationsText))
    print(len(allCombinationsText))
    exit('Done!')
    # print(allCombinationsText)
    print('共有%s种人物组合属性' % len(allCombinations))
    count = 0
    newCombinations = []
    for item in allCombinations:
        target = item.values()
        if '攻击' in target or '暴击率' in target or '暴击伤害' in target or '增加技能命中' in target or '气血' in target:
            count += 1
            newCombinations.append(item)
    print('其中有%s种人物组合符合您的期望' % count)
    # print('var combinations = [')
    # for item in newCombinations:
    #     print('{')
    #     print('name :', '"' + item['name'] + '"', end=',\n')
    #     print('combinationName :', '"' + item['combinationName'] + '"', end=',\n')
    #     print('tiaoJian :', '"' + item['tiaoJian'] + '"', end=',\n')
    #     print('activateProperty :', '"' + item['activateProperty'] + '"', end=',\n')
    #     print('}',end=',// %s",\n' % item['name'])
    # print('];')
    print('请刷新网页，来获取最新人物组合属性。')
# try:
#     full_txt = title_txt.readlines()
#     regex1 = "/A/d*[/n]/Z"
#     regex2 = "/d --> /d"
#     #print full_txt
#     new_txt = []
#     for line in full_txt:
#         #print line
#         if re.match(regex1, line) or re.search(regex2, line):
#             #print "match", line
#             continue
#         else:
#             new_txt.append(line)

#     title_txt.seek(0)
#     title_txt.truncate(0)
#     #for line in full_txt:
#     #    title_txt.writelines(line)
#     title_txt.writelines(new_txt)

# finally:
#     title_txt.close()

# print "Over"