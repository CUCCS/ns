# -*- coding: utf-8 -*-
import re
import numpy as np
from sklearn import cross_validation
from sklearn import datasets
from sklearn import svm
from sklearn.externals import  joblib
from sklearn.metrics import classification_report
from sklearn import metrics

#存放提取的特征
data = []
#数据打标;1为xss;0为正常
tap = []

#特征提取时使用函数
def get_len(url):
    return len(url)

def get_url_count(url):
    if re.search('(http://)|(https://)', url, re.IGNORECASE) :
        return 1
    else:
        return 0

def get_evil_char(url):
    return len(re.findall("[<>,\'\"/]", url, re.IGNORECASE))

def get_evil_word(url):
    return len(re.findall("(alert)|(script=)(%3c)|(%3e)|(%20)|(onerror)|(onload)|(eval)|(src=)|(prompt)",url,re.IGNORECASE))

def get_last_char(url):
    if re.search('/$', url, re.IGNORECASE) :
        return 1
    else:
        return 0

def get_feature(url):
    return [get_len(url),get_url_count(url),get_evil_char(url),get_evil_word(url),get_last_char(url)]

#结果输出
def do_metrics(y_test,y_pred):
    #分类准确率：所有分类正确的百分比
    print ("metrics.accuracy_score:")
    print (metrics.accuracy_score(y_test, y_pred))
    #混淆矩阵：判断存在问题，进行改进
    print ("metrics.confusion_matrix:")
    print (metrics.confusion_matrix(y_test, y_pred))
    #tp / (tp + fp)
    print ("metrics.precision_score:")
    print (metrics.precision_score(y_test, y_pred))
    #召回率：tp / (tp + fn)
    print ("metrics.recall_score:")
    print (metrics.recall_score(y_test, y_pred))
    #F1 = 2 * (precision * recall) / (precision + recall)
    print ("metrics.f1_score:")
    print (metrics.f1_score(y_test,y_pred))

#提取特征，数据打标
def etl(filename,data,isxss):
        with open(filename) as f:
            for line in f:
                f1=get_len(line)
                f2=get_url_count(line)
                f3=get_evil_char(line)
                f4=get_evil_word(line)
                data.append([f1,f2,f3,f4])
                if isxss:
                    tap.append(1)
                else:
                    tap.append(0)
        return data

#xss-10000.txt中包含处理过的10000条xss攻击数据
etl('xss-10000.txt',data,1)
#good-xss-10000.txt中包含处理过的1000条正常数据
etl('good-xss-10000.txt',data,0)

#随机的把数据拆分为训练组和测试组，此处设置40%作为测试数据，60%作为训练数据
x_train, x_test, y_train, y_test = cross_validation.train_test_split(data,tap, test_size=0.4, random_state=0)

#使用Scikit-Learn的SVM模型进行分类
clf = svm.SVC(kernel='linear', C=1).fit(x_train, y_train)
#print(x_train)
#print(y_train)

#获得预测结果
y_pred = clf.predict(x_test)
#print(y_pred)

#获得准确率、召回率等数据
do_metrics(y_test, y_pred)

#保存模型
joblib.dump(clf,"xss-svm-10000-module.m")
