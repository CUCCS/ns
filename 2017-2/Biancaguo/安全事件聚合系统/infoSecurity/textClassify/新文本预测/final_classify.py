#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#对新文本进行分词
import text_split
def text_split_new():
    file_name = "text.txt"  # 未分词分类语料库路径
    seg_path = "./after/"  # 分词后分类语料库路径
    text_split.corpus_segment(file_name, seg_path)

# 对新文本进行Bunch化操作
import bunch
def bunch_new():
    wordbag_name = "./after/text.dat"  # Bunch存储路径
    seg_name = "./after/text.txt"  # 分词后分类语料库路径
    bunch.corpus2Bunch(wordbag_name, seg_name)

#对新文本计算权重
import TF_IDF

def tf_idf_new():
    stopword_path = "./after/hlt_stop.txt"
    bunch_path = "./after/text.dat"
    space_path = "./after/textspace.dat"
    train_tfidf_path = "./after/tfdifspace.dat"
    TF_IDF.vector_space(stopword_path, bunch_path, space_path, train_tfidf_path)


import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import cPickle as pickle
from sklearn.naive_bayes import MultinomialNB  # 导入多项式贝叶斯算法

# 读取bunch对象
def _readbunchobj(path):
    with open(path, "rb") as file_obj:
        bunch = pickle.load(file_obj)
    return bunch

def specific_new():
    # 导入训练集
    trainpath = "./after/tfdifspace.dat"
    train_set = _readbunchobj(trainpath)

    # 导入测试集
    testpath = "./after/textspace.dat"
    test_set = _readbunchobj(testpath)

    # 训练分类器：输入词袋向量和分类标签，alpha:0.001 alpha越小，迭代次数越多，精度越高
    clf = MultinomialNB(alpha=0.001).fit(train_set.tdm, train_set.label)

    # 预测分类结果
    predicted = clf.predict(test_set.tdm)

    expct_cate=predicted
    print "预测类别:",expct_cate[0].decode('gbk').encode('utf8')
    print "预测完毕!!!"

if __name__ == '__main__':
	import MySQLdb
	# 打开数据库连接
	db=MySQLdb.connect(host='localhost',user='root',passwd='123',db='Spider',charset='utf8')

	# 使用cursor()方法获取操作游标 
	cursor = db.cursor()

	choices=["SpiderForCnbeta","SpiderFor36ker","SpiderFor51CTO"]
	# SQL 查询语句

	for choice in choices:
		id=0
		sql = "SELECT `abstraction` FROM "+choice
		# 执行SQL语句
		cursor.execute(sql)
		# 获取所有记录列表
		results = cursor.fetchall()
		for row in results:
			id=id+1
			s="".join(row)
			with open("text.txt","w") as f:
			 f.write(s.encode("utf-8"))


			text_split_new()

			bunch_new()

			tf_idf_new()

			specific_new(choice,id)
		
                    
	# 关闭数据库连接
	db.close()




