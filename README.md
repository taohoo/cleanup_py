# cleanup
clean files and directories.
# 从pip安装
```commandline
pip install bb_cleanup
```
# 编译安装
```
python -m build
# twine upload dist/*   # 发布到到pipy，作者专用
pip install .\dist\bb_cleanup-0.1.11-py3-none-any.whl
```
# 命令行
```
cleanup --help
```
# .clean文件和参数说明
```
# 需要清除的文件夹匹配表达式
dir_patterns = dist,log,__pycache__,tmp,.pytest_cache
# 需要清除的文件的匹配表达式
file_patterns = *.pyc
# 清除时回避符合如下开头的路径
exclude_patterns = ./venv/*
```
