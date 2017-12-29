#usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import os
import jieba

# 配置utf-8输出环境
reload(sys)
sys.setdefaultencoding('utf-8')


# 保存至文件
def savefile(savepath, content):
    with open(savepath, "wb") as fp:
        fp.write(content)

# 读取文件
def readfile(path):
    with open(path, "rb") as fp:
        content = fp.read()
    return content


def corpus_segment(corpus_name, seg_path):
        if not os.path.exists(seg_path):  # 是否存在分词目录，如果没有则创建该目录
            os.makedirs(seg_path)
        content = readfile(corpus_name)  # 读取文件内容
        content = content.replace("\r\n", "")  # 删除换行
        content = content.replace(" ", "")  # 删除空行、多余的空格
        content_seg = jieba.cut(content)  # 为文件内容分词
        savefile(seg_path+corpus_name, " ".join(content_seg))  # 将处理后的文件保存到分词后语料目录
        print "新文本分词结束！！！"



