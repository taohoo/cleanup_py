# -*- coding: utf-8 -*-
"""
@author: hubo
@project: bb-py
@file: cleanup_test.py
@time: 2023/11/21 21:41
@desc:
"""
import warnings

from ..cleanup import cleanup
from ..command import main


def test_clean():
    patterns = ['dist', 'log', '__pycache__', 'tmp', '.pytest_cache', '*.pyc']  # to remove
    excludes = ['./venv*']  # to exclude
    cleanup(patterns, excludes)


def test_run():
    import os
    import sys
    sys.argv = sys.argv[:1]
    print(os.getcwd())
    # os.chdir('../..')
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        main()
        for warning in w:
            print(warning.message)
