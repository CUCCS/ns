#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import os  # python内置的包，用于进行文件目录操作，我们将会用到os.listdir函数
import cPickle as pickle  # 导入cPickle包并且取一个别名pickle

from sklearn.datasets.base import Bunch



def _readfile(path):
    with open(path, "rb") as fp:  # with as句法前面的代码已经多次介绍过，今后不再注释
        content = fp.read()
    return content


def corpus2Bunch(wordbag_name, seg_name):
    #catelist = os.listdir(seg_path)  # 获取seg_path下的所有子目录，也就是分类信息
    # 创建一个Bunch实例
    bunch = Bunch(contents=[])
    fullname = seg_name  # 拼出文件名全路径
    bunch.contents.append(_readfile(fullname))  # 读取文件内容
    with open(wordbag_name, "wb") as file_obj:
        pickle.dump(bunch, file_obj)
    print "构建文本对象结束！！！"
