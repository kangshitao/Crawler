# 正则表达式的练习，re库的使用
# re库采用raw string（原生字符串，不包含转义字符）类型表示正则表达式，表示为r'text'
# 例如：r'[1-9]\d{5}' 表示六位数字的邮政编号

import re

# search函数,re.search(pattern, string, flags=0),从string中搜索匹配pattern的第一个位置，返回match对象
# 此处的match对象仅为一次匹配的结果
print('search函数：')
match_se = re.search(r'[1-9]\d{5}', 'BIT 100081，123456')
if match_se:
    print(match_se.group(0))  # group(0)获取匹配后的字符串
    print("匹配的正则表达式：", match_se.re, '搜索的开始位置：', match_se.pos, '搜索的结束位置：', match_se.endpos)
    print('结果的开始位置：', match_se.start(), '结果的结束位置：', match_se.end())

# match函数,re.match(pattern, string, flags=0),从string的开始位置起匹配pattern，返回match对象
print('match函数：')
match_ma = re.match(r'[1-9]\d{5}', 'BIT 100081，123456')  # 此时字符串是以字母开头的，所以匹配结果为空
match_ma_2 = re.match(r'[1-9]\d{5}', '100081，123456')
if match_ma:
    print('1:', match_ma.group(0))

if match_ma_2:
    print('2:', match_ma_2.group(0))

# findall函数，re.findall(pattern, string, flags=0),搜索字符串，以列表类型返回全部能匹配的子串
print('findall函数：')
match_find = re.findall(r'[1-9]\d{5}', 'BIT 100081，123456')
if match_find:
    print(match_find)

# split函数，re.split(pattern, string, maxsplit = 0, flags=0) ,将string按照正则表达式匹配结果进行分割，返回列表类型
# maxsplit表示最大分割数，超过设定值的剩余子串将作为最后一个元素输出
print('split函数：')
match_sp = re.split(r'[1-9]\d{5}', 'BIT100081 123456TSU')
if match_sp:
    print(match_sp)

# finditer函数，re.finiter(pattern, string, flags=0),搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match元素
print('finditer函数：')
for m in re.finditer(r'[1-9]\d{5}', 'BIT100081 123456TSU'):
    if m:
        print(m.group(0))

# sub函数，re.sub(pattern, repl, string, count=0, flags=0),将string中与pattern匹配的子串替换为repl，并返回替换结果字符串
# count表示最大替换次数
sub = re.sub(r'[1-9]\d{5}','zipcode', 'BIT100081 123456TSU')
print(sub)

# compile函数，面向对象编程常用的函数，将正则表达式的表示编译为正则表达式
# re.search() 等价于 regex = re.compile(), regex.search() 
print('compile函数：')
regex = re.compile(r'[1-9]\d{5}')  # 此时regex就表示正则表达式[1-9]\d{5}
print(regex.search('BIT 100081，123456').group(0))  # 其函数用法与未编译用法一致，不过是没有了pattern参数


'''
# re的贪婪匹配原则：返回匹配结果最长的字符串
# 当有字符串满足不同长度的匹配规则时，可以通过添加‘？’获得最小匹配结果
'''
rt = re.search(r'py.*n', 'pyanbncndn')
print('贪婪匹配结果：', rt.group(0))
# 最小匹配只需要加‘？’即可
rm = re.search(r'py.*?n', 'pyanbncndn')
print('最小匹配结果：', rm.group(0))

