#!/usr/bin/env python
# coding:utf8

"""
usage:
    作用: 删除文件名称中的部分内容
    使用: 将本脚本放入文件夹中, 执行以下命令
    python rename.py name1 [name2] [ignore-path] [ignore-ext]
    name1 如果文件名中有 name1 ，则这部分会被移除
    name2 可选，会移除文件名中 name1 到 name2 的内容，不包括name2
    ignore-path: 可选，忽略的目录。有默认忽略选项，请使用 , 将要忽略的目录列出
    ignore-ext: 可选，忽略的文件后缀，比如 .exe, .mp4。有默认的忽略选项，请使用 , 将要忽略的目录列出

    示例: python del.py 文本1 none .git,.ssh -> name1: 文本1, name2: none, ignore_path: ['.git', '.ssh'], ignore_ext: ['']
"""

import os
import sys

default_ignore_ext = ['']


def delname(path, name1, name2, ignore_ext):
    for item in os.listdir(path):
        if item == 'del.py':
            continue
        if os.path.isfile(item):
            execute(item, name1, name2, ignore_ext)


def execute(item, name1, name2, ignore_ext):
    if ignore_ext:
        # 取文件后缀名称
        ext = os.path.splitext(item)[1]
        if ext in ignore_ext:
            return

    rep = name1
    if name2:
        pos1 = item.find(name1)
        if pos1 == -1:
            return
        pos2 = item.find(name2)
        if pos2 != -1:
            rep = item[pos1:pos2]
    newname = item.replace(rep, '')
    if newname != item:
        rename(item, newname)


def rename(item, newname):
    os.rename(item, newname)
    print "[rename] item: {}, newname: {}".format(item, newname)


if __name__ == '__main__':
    n = len(sys.argv)
    if n == 1:
        print __doc__
        exit()
    name1 = sys.argv[1]
    name2 = None
    ignore_ext = default_ignore_ext
    if (n > 2):
        name2 = sys.argv[2]
        if (n > 3):
            ext = sys.argv[3]
            if ext:
                ignore_ext = ext.split(',')
    print "name1: {}, name2: {}, ignore_ext: {}".format(name1, name2, ignore_ext)
    delname('.', name1, name2, ignore_ext)
