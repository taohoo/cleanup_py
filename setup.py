# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='bb_cleanup',
    version='0.1.31',
    description='clean files and directories using Unix-Shell Style wildcards',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='HuBo',
    author_email='taohoo@163.com',
    url='https://github.com/taohoo/bb-cleanup',
    license='MIT License',
    packages=find_packages(),
    platforms=['all'],
    python_requires='>=3.6',
    include_package_data=True,  # 打包python发行包中的include和libs，对应配置在MANIFEST.in中，
    install_requires=['environs'],
    entry_points={'console_scripts': ['cleanup = bb_cleanup.command:main']},
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
)
