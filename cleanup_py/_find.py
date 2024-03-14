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


def find(directory, pattern):
    """
    Find all directories or file lists in the directory that match the pattern, including all subdirectories
    :param directory: directory
    :param pattern: pattern, with Unix-Shell style wildcard
    :return:
    """
    finds = []
    for root, dirs, files in os.walk(directory):
        for dir in dirs:
            path = os.path.join(root, dir)
            if fnmatch.fnmatch(dir, pattern) or fnmatch.fnmatch(path, pattern):
                finds.append(path)
        for file in files:
            path = os.path.join(root, file)
            if fnmatch.fnmatch(file, pattern) or fnmatch.fnmatch(path, pattern):
                finds.append(path)
    return finds
