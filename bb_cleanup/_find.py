# -*- coding: utf-8 -*-
"""
@author: hubo
@project: cleanup
@file: _find.py
@time: 2023/12/26 13:53
@desc:
"""
import os
import fnmatch


def find(directory, pattern, mode='df'):
    """
    在目录中查找符合pattern的所有目录或者文件清单，包含所有子目录
    :param directory: 指定的目录
    :param pattern: 表达式，支持通配符
    :param mode: 模式，d标识目录，f标识文件，可用于只返回文件还是只返回目录
    :return:
    """
    finds = []
    for root, dirs, files in os.walk(directory):
        if 'd' in mode:
            for dir in dirs:
                path = os.path.join(root, dir)
                if fnmatch.fnmatch(dir, pattern) or fnmatch.fnmatch(path, pattern):
                    finds.append(path)
        if 'f' in mode:
            for file in files:
                path = os.path.join(root, file)
                if fnmatch.fnmatch(file, pattern) or fnmatch.fnmatch(path, pattern):
                    finds.append(path)
    return finds
