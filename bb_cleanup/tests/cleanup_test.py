# -*- coding: utf-8 -*-
"""
@author: hubo
@project: bb-py
@file: cleanup_test.py
@time: 2023/11/21 21:41
@desc:
"""
from ..cleanup import cleanup
from ..command import main


def test_clean():
    dir_patterns = ['dist', 'log', '__pycache__', 'tmp', '.pytest_cache']  # 要清理的目录清单
    file_patterns = ['*.pyc']  # 要清理的文件清单
    exclude_patterns = ['./venv*']  # 不清理以这些打头的

    cleanup(dir_patterns, file_patterns, exclude_patterns)


def test_run():
    import os
    import sys
    sys.argv = sys.argv[:1]
    print(os.getcwd())
    os.chdir('..')
    main()
