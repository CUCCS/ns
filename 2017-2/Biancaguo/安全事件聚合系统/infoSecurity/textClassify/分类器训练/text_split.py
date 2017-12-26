#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""

"""
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


def corpus_segment(corpus_path, seg_path):
   
    catelist = os.listdir(corpus_path)  # 获取corpus_path下的所有子目录

    # 获取每个目录（类别）下所有的文件
    for mydir in catelist:
     
        class_path = corpus_path + mydir + "/"  # 拼出分类子目录的路径
        seg_dir = seg_path + mydir + "/"  # 拼出分词后存贮的对应目录路径

        if not os.path.exists(seg_dir):  # 是否存在分词目录，如果没有则创建该目录
            os.makedirs(seg_dir)

        file_list = os.listdir(class_path)  # 获取未分词语料库中某一类别中的所有文本
       
        for file_path in file_list:  # 遍历类别目录下的所有文件
            fullname = class_path + file_path  # 拼出文件名全路径
            content = readfile(fullname)  # 读取文件内容
            content = content.replace("\r\n", "")  # 删除换行
            content = content.replace(" ", "")  # 删除空行、多余的空格
            content_seg = jieba.cut(content)  # 为文件内容分词
            savefile(seg_dir + file_path, " ".join(content_seg))  # 将处理后的文件保存到分词后语料目录

    print "中文语料分词结束！！！"


if __name__ == "__main__":
    # 对训练集进行分词
    corpus_path = "./data/train/"  # 未分词分类语料库路径
    seg_path = "./after/train/"  # 分词后分类语料库路径
    corpus_segment(corpus_path, seg_path)

    # 对测试集进行分词
    corpus_path = "./data/test/"  # 未分词分类语料库路径
    seg_path = "./after/test/"  # 分词后分类语料库路径
    corpus_segment(corpus_path, seg_path)


