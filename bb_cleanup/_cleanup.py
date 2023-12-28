# -*- coding: utf-8 -*-
"""
@author: hubo
@project: bb-py
@file: _clean.py
@time: 2023/11/21 19:59
@desc:
"""


import fnmatch
import os


def _format_pattern(pattern):
    pattern = pattern.replace('\\', os.sep).replace('/', os.sep)
    return pattern


def _fnmatch_in(path, patterns):
    """判断字符串s是否以列表l中的某个item开头"""
    file_or_dir_name = os.path.split(path)[1]
    for pattern in patterns:
        if fnmatch.fnmatch(file_or_dir_name, pattern) or fnmatch.fnmatch(path, pattern):
            return True
    return False
