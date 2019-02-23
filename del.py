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
    abspath = os.path.abspath(path)
    for root, dirs, files in os.walk(abspath, topdown=False):
        if ".git" in root:
            continue
        # 先修改文件名称
        for file in files:
            rename(root, file, name1, name2, ignore_ext)
        # 再修改文件夹名称
        for dir in dirs:
            rename(root, dir, name1, name2, ignore_ext)


def rename(root, path, name1, name2, ignore_ext):
    if ignore_ext and os.path.isfile(path):
        ext = os.path.splitext(path)[1]
        if ext in ignore_ext:
            return

    filepath = os.path.join(root, path)
    newpath = getnewname(path, name1, name2)
    newfilepath = os.path.join(root, newpath)
    os.rename(filepath, newfilepath)
    print '[rename] {} -> {}'.format(path, newpath)


def getnewname(path, name1, name2):
    rep = name1
    if name2:
        pos1 = path.find(name1)
        if pos1 == -1:
            return path
        pos2 = path.find(name2)
        if pos2 != -1:
            rep = path[pos1:pos2]
    newname = path.replace(rep, '')
    return newname


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
