# -*- coding: utf-8 -*-
"""
@author: hubo
@project: bb-py
@file: main.py
@time: 2023/11/27 11:44
@desc:
"""
import os
import re
import argparse
import warnings

from environs import Env

from ._cleanup import _format_pattern
from .cleanup import cleanup


def _str_2_list(s):
    return [i.strip() for i in s.split(',')]


def _warn(patterns, excludes):
    """Detect invalid configurations and provide some suggestions"""
    cwd = './'.replace('/', os.sep)
    re_pattern = os.sep.replace('\\', '\\\\')
    for pattern in patterns + excludes:
        pattern = _format_pattern(pattern)
        # 不是以cwd或者*开头，但是包含了os.sep是无法匹配的
        if (not pattern.startswith(cwd) and not pattern.startswith('*')
                and len(re.findall(re_pattern, pattern)) >= 1):
            _path_pattern = os.path.normpath(pattern)
            maybes = f"{cwd}{_path_pattern} *{_path_pattern}"
            # 可能多添加了os.sep或者*
            maybes = maybes.replace(f"{os.sep}{os.sep}", f"{os.sep}").replace('**', '*')
            warnings.warn(f"{pattern} is invalid. Maybe you want: {maybes}")
        # 以os.sep结尾是无法匹配的
        elif pattern.endswith(os.sep):
            warnings.warn(f"{pattern} is invalid. Maybe you want: {pattern[:-1]}")


def main():
    """After pip installation, it can be executed directly from the command line"""
    parser = argparse.ArgumentParser(description='Clean up the current folder')
    parser.add_argument('config_file', nargs='?', type=str, default='.cleanup', help='Configuration file, default to .cleanup in the current working directory')
    parser.add_argument('-p', '--patterns', default='',
                        help='Matching expressions for folders and files, using Unix Shell style. If there are multiple expressions, use commas to separate them')
    parser.add_argument('-e', '--excludes', default='',
                        help='Match expressions for files or folders that are not cleaned, using Unix Shell style. If there are multiple expressions, use commas to separate them')
    args = parser.parse_args()

    patterns = [] if args.patterns == '' else _str_2_list(args.patterns)
    excludes = [] if args.excludes == '' else _str_2_list(args.excludes)

    # Check if the configuration file exists
    if os.path.exists(args.config_file):
        if len(patterns) or len(excludes):
            print(f"{args.config_file} exists, the args in command are ignored.")
        env = Env()
        env.read_env(args.config_file)
        # environs中的strip好像只针对原始配置中的字符串，而不针对解析为list之后的字符元素
        patterns = _str_2_list(env.str('patterns', metadata={'strip': True}))
        excludes = _str_2_list(env.str('excludes', metadata={'strip': True}))
    if len(patterns) == 0 and len(excludes) == 0:
        parser.print_help()
        exit(0)
    _warn(patterns, excludes)
    cleanup(patterns, excludes)
