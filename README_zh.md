# cleanup
用UNIX Shell风格的通配符清理文件和文件夹。
可以在一条命令中使用多个删除参数，也可以将参数写到文件，以方便反复执行。
# 从pip安装
```
pip install bb_cleanup
```
# 编译安装
```
python -m build
pip install .\dist\bb_cleanup-0.1.31-py3-none-any.whl
```
# 命令行
```
cleanup --help
```
# .clean文件和参数说明
```
# 需要清除的文件或文件夹的匹配表达式
patterns = dist,log,__pycache__,tmp,.pytest_cache,*.pyc
# 清除时需要排除的文件或文件夹的表达是
excludes = ./venv/*
```