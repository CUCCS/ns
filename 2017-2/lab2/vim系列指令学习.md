# vim系列指令学习

## 视频地址

chap1：https://asciinema.org/a/2nJZu0kfCAslBluJStA87ll0i

chap2：https://asciinema.org/a/LytiOXfliAOlweHNDRjMK3ybe

chap3：https://asciinema.org/a/mdPw1Khr4iJw1tISkaFZnawpk

chap4：https://asciinema.org/a/EduooiScGY0T2BcrjhSPgjDZI

chap5：https://asciinema.org/a/0I5ZYW23ave6uvuhBydG47D4y

chap6：https://asciinema.org/a/zGHT2GFmdekPSbg2kk7TbZKDc

chap7：https://asciinema.org/a/bLy3CLXmuTB2ecxUBKQurbsUv

## 自查清单

* vim有三种工作模式

  * 命令模式。部分指令可以直接被执行。如'dd'是删除掉一整行。'2w'是向后跳两个单词等。
  * 插入模式。执行输入字符等操作。
  * 底线命令模式。在命令模式下按下':'就进入了底线命令模式。一般用来保存退出等操作。

* Normal模式下

  * 一次向下移动光标10行：```10j```
  * 快速移动到开始行：```gg```
  * 快速移动到结束行：```G```
  * 跳转到文件第N行：```NG```


  * 删除单个字符：```x```
  * 删除单个单词：```dw```
  * 从当前光标一直删除到行尾：```d$```
  * 从当前光标只删除单行：```dd```
  * 从当前光标一直删除到当前行向下数n行：

* 在vim中快速插入N个空行：```N i<Enter><Esc><Esc>```

* 在vim中快速插入80个'-'：```80i-<Esc><Esc>```

* 撤销最近一次编辑操作：```o```

* 重做最近一次被撤销的操作：```CTRL+R```

* 剪切粘贴单个字符：```x p```

* 剪切粘贴单词：```dw p```

* 复制粘贴操作：按```v```进入visual mode，选中要复制的内容，按```y```，在要粘贴的地方按```p```

* 编辑文本的按键序列

  * ```vim filename```
  * normal mode下，使用```kjhl```控制光标上下左右移动
  * 编辑文本
  * 使用```:wq!```保存并退出

* 查看当前正在编辑的文件名：```CTRL+g```

* 查看当前所在行号：```CTRL+g```

* 文件中关键词搜索

  * 普通模式： ```/keyword```
  * 忽略大小写：```:set ic```
  * 匹配结果高亮显示：```set hls is```
  * 匹配结果批量替换：```s/old/new/g```
  * 在两行间批量替换：```:#,#s/old/new/g```
  * 在全文中批量替换```:%s/old/new/g```

* 最近编辑过的位置来回跳转：

  * 以前```CTRL+o```
  * 以后```CTRL+I```

* 定位括号匹配项```%```

* 在不退出vim的情况下执行外部程序：```:!command```

  * 如```:!ls```

* 用vim的内置帮助系统查询内置默认快捷键```:help name```

* 在两个不同的分屏窗口中移动光标：```CTRL+w```