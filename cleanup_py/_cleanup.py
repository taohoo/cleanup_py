# -*- coding: utf-8 -*-
"""
@author: hubo
@project: cleanup_py
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
    """Determine if the path matches any wildcard character in the patterns"""
    # 先检查全路径是否匹配
    for pattern in patterns:
        if fnmatch.fnmatch(path, pattern):
            return True
    # 把每个目录和文件名截出来再匹配一次
    while True:
        path, part = os.path.split(path)
        if part != "":
            for pattern in patterns:
                if fnmatch.fnmatch(part, pattern):
                    return True
        else:
            break

    return False
