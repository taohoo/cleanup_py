# -*- coding: utf-8 -*-
"""
@author: hubo
@project: bb-py
@file: clean.py
@time: 2023/11/21 19:59
@desc:
"""
import os
import shutil

from ._cleanup import _fnmatch_in, _format_pattern
from ._find import find


def cleanup(dir_patterns, file_patterns, exclude_patterns=[]):
    '''
    针对当前工作文件夹进行清理
    :param dir_patterns: list of directory patterns
    :param file_patterns: list of file patterns
    :param exclude_patterns: list of exclude patterns
    :return:
    '''
    # 做一些处理，确保格式一致
    dir_patterns = [_format_pattern(i) for i in dir_patterns]
    file_patterns = [_format_pattern(i) for i in file_patterns]
    exclude_patterns = [_format_pattern(i) for i in exclude_patterns]
    cwd = './'.replace('/', os.sep)
    for dir_pattern in dir_patterns:
        dirs = find(cwd, dir_pattern, mode='d')
        for dir in dirs:
            if os.path.exists(dir) and not _fnmatch_in(dir, exclude_patterns):
                shutil.rmtree(dir)
                print(f"删除目录: {dir_pattern} {dir}")
    for file_pattern in file_patterns:
        files = find(cwd, file_pattern, mode='f')
        # files = [os.path.normpath(i) for i in files]
        for file in files:
            if os.path.exists(file) and not _fnmatch_in(file, exclude_patterns):
                os.remove(file)
                print(f"删除文件: {file_pattern} {file}")
