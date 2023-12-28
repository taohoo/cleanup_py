# cleanup
clean files and directories using Unix-Shell Style wildcards.
# Installing with pip
```commandline
pip install bb_cleanup
```
# # Installing with building
```
python -m build
pip install .\dist\bb_cleanup-0.1.20-py3-none-any.whl
```
# Command
```
cleanup --help
```
```
usage: cleanup [-h] [-p PATTERNS] [-e EXCLUDES] [config_file]

Clean up the current folder

positional arguments:
  config_file           Configuration file, default to .cleanup in the current working directory

options:
  -h, --help            show this help message and exit
  -p PATTERNS, --patterns PATTERNS
                        Matching expressions for folders and files, using Unix Shell style. If there are multiple expressions, use commas to separate them    
  -e EXCLUDES, --excludes EXCLUDES
                        Match expressions for files or folders that are not cleaned, using Unix Shell style. If there are multiple expressions, use commas    
                        to separate them
```
# Using .clean
```
# Matching expressions for folders and files, using Unix Shell style. If there are multiple expressions, use commas to separate them
patterns = dist,log,__pycache__,tmp,.pytest_cache,*.pyc
# Match expressions for files or folders that are not cleaned, using Unix Shell style. If there are multiple expressions, use commas to separate them
exclude_patterns = ./venv/*,*.tar.gz
```
