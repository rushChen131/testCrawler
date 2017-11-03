# -*-coding:utf-8-*-
# 作者：华亮
import os

xml = '''
<background>
  <starttime>
    <year>2009</year>
    <month>08</month>
    <day>04</day>
    <hour>00</hour>
    <minute>00</minute>
    <second>00</second>
  </starttime>
'''

static_duration = 10  # 一张壁纸的停留时间
trasition_duration = 1  # 切换时间


def CreateStatic(duration, file):
    return '<static>\n\t<duration>' + str(duration) + '</duration>\n\t<file>' + str(file) + '</file>\n</static>\n'


def CreateTransition(duration, fromFile, toFile):
    return '<transition>\n\t<duration>' + str(duration) + '</duration>\n\t<from>' + str(
        fromFile) + '</from>\n\t<to>' + str(toFile) + '</to>\n</transition>\n'


# 读取当前目录下所有文件
images = []
for filename in os.listdir(os.getcwd()):
    root, ext = os.path.splitext(filename)
    if ext.lower() == '.bmp' or '.jpg' or '.png':
        images.append(os.path.join(os.getcwd(), filename))
# 生成XML
for i in range(len(images) - 1):
    xml += CreateStatic(static_duration, images[i]) + CreateTransition(trasition_duration, images[i], images[i + 1])
xml += CreateStatic(static_duration, images[len(images) - 1]) + CreateTransition(trasition_duration,
                                                                                 images[len(images) - 1],
                                                                                 images[0]) + '</background>'
# 保存文件
file = open(os.path.basename(os.getcwd()) + ".xml", 'w')
file.write(xml)
file.close()

