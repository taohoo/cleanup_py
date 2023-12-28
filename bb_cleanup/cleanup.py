# -*- coding: utf-8 -*-
"""
@author: hubo
@project: bb-py
@file: clean.py
@time: 2023/11/21 19:59
@desc:
"""
import os

from ._cleanup import _fnmatch_in, _format_pattern
from ._find import find


def cleanup(patterns, excludes=[], cwd=None):
    '''
    Clean up folders
    :param patterns: list of patterns
    :param excludes: list of exclude patterns
    :return: None
    '''
    # 做一些处理，确保格式一致
    patterns = [_format_pattern(i) for i in patterns]
    excludes = [_format_pattern(i) for i in excludes]
    if not cwd:
        cwd = './'.replace('/', os.sep)
    for pattern in patterns:
        pathes = find(cwd, pattern)
        for path in pathes:
            if os.path.exists(path) and not _fnmatch_in(path, excludes):
                if os.path.isdir(path):
                    _remove_dir(path, pattern, excludes)
                else:
                    _remove_file(path, pattern)


def _remove_dir(path, pattern, excludes):
    """Clean up the directory that has already been matched,
     but keep the files or folders that need to be excluded"""
    for child in os.listdir(path):
        child_path = os.path.join(path, child)
        if not _fnmatch_in(child_path, excludes):
            if os.path.isdir(child_path):
                _remove_dir(child_path, pattern, excludes)
            else:
                _remove_file(child_path, pattern)
    if len(os.listdir(path)) == 0:
        os.rmdir(path)
        print(f"Removed: {pattern} {path}")


def _remove_file(path, pattern):
    """remove mathed file"""
    os.remove(path)
    print(f"Removed: {pattern} {path}")
