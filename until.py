#-*- coding:utf-8 -*-
import jieba

import test
import re  # 正则表达式库
import collections  # 词频统计库
import numpy as np  # numpy数据处理库
import jieba  # 结巴分词
import wordcloud  # 词云展示库
from PIL import Image  # 图像处理库
import matplotlib.pyplot as plt  # 图像展示库


#通过读取文本文件分析
def word_top(str):
    article = open('data/'+str+'.txt', 'r',encoding='utf-8').read()
    dele = {'。','！','？','的','“','”','（','）',' ','》','《','，','你们','自己','我们','他们'}
    words = list(jieba.cut(article))
    articleDict = {}
    articleSet = set(words)-dele
    for w in articleSet:
        if len(w)>1:
            articleDict[w] = words.count(w)

    articlelist = sorted(articleDict.items(),key = lambda x:x[1], reverse = True)
    return articlelist

#通过读字符串
def word_top_string(str):
    dele = {'。','！','？','的','“','”','（','）',' ','》','《','，','你们','自己','我们','他们'}
    words = list(jieba.cut(str))
    articleDict = {}
    articleSet = set(words)-dele
    for w in articleSet:
        if len(w)>1:
            articleDict[w] = words.count(w)

    articlelist = sorted(articleDict.items(),key = lambda x:x[1], reverse = True)
    return articlelist

def analysis(name):
    # 读取文件
    fn = open('F:\\PyCharm\\newsProject\\file\\mytest.csv', 'rt', encoding='utf-8')  # 打开文件
    string_data = fn.read()  # 读出整个文件
    fn.close()  # 关闭文件

    # 文本预处理
    pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?| |"')  # 定义正则表达式匹配模式
    string_data = re.sub(pattern, '', string_data)  # 将符合模式的字符去除

    # 文本分词
    seg_list_exact = jieba.cut(string_data, cut_all=False)  # 精确模式分词
    object_list = []
    # remove_words = [u'》', u'，', u'：', u'。', u' ', u'、', u'“', u'"', u'"', u":", u'《', u'”']  # 自定义去除词库

    # 分词并去除停用词
    remove_words = set()
    fr = open('F:\\PyCharm\\newsProject\\stopword\\stopword.txt', encoding='UTF-8')
    for word in fr:
        remove_words.add(str(word).strip())
    fr.close()

    for word in seg_list_exact:  # 循环读出每个分词
        if word not in remove_words:  # 如果不在去除词库中
            object_list.append(word)  # 分词追加到列表

    # 词频统计
    word_counts = collections.Counter(object_list)  # 对分词做词频统计
    word_counts_top10 = word_counts.most_common(100)  # 获取前10最高频的词
    print(word_counts_top10)  # 输出检查

    # 词频展示
    mask = np.array(Image.open(''))  # 定义词频背景
    wc = wordcloud.WordCloud(
        font_path='F:\\PyCharm\\newsProject\\file\\simhei.ttf',  # 设置字体格式
        mask=mask,  # 设置背景图
        max_words=200,  # 最多显示词数
        max_font_size=100  # 字体最大值
    )

    wc.generate_from_frequencies(word_counts)  # 从字典生成词云
    image_colors = wordcloud.ImageColorGenerator(mask)  # 从背景图建立颜色方案
    wc.recolor(color_func=image_colors)  # 将词云颜色设置为背景图方案
    plt.imshow(wc)  # 显示词云
    plt.axis('off')  # 关闭坐标轴
    plt.show()  # 显示图像

#通过读取数据库
def find_word_bySql(type):
    sql=""
    if(type=="all"):
        sql="select * from result_data"
    elif(type=="a"):
        sql="select * from result_ty"
    elif(type=="b"):
        sql="select * from result_zhty"
    elif(type=="c"):
        sql="select * from result_js"
    elif(type=="d"):
        sql="select * from result_yl"
    elif(type=="e"):
        sql="select * from result_tyjd"
    elif(type=="f"):
        sql="select * from result_fc"
    elif(type=="g"):
        sql="select * from result_jy"
    elif(type=="h"):
        sql="select * from result_qc"
    elif(type=="i"):
        sql="select * from result_game"
    elif (type == "j"):
        sql = "select * from result_kj"
    elif(type=="k"):
        sql="select * from result_cj"
    res=test.query_mysql(sql)
    return res

if __name__ == '__main__':
    # data_all=test.find_type("财经")
    # str=""
    # flag=1
    # for i in data_all:
    #     str=str+i[0]
    #     print(flag)
    #     flag=flag+1
    # fh = open('data/k.txt', 'w', encoding='utf-8')
    # fh.write(str)
    # fh.close()
    word_top("b")
    pass