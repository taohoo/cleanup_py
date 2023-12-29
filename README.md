# cleanup
Clean files and directories using Unix-Shell Style wildcards.
Multiple clean parameters can be used in a single command, or they can be written to a file for easy execution.
# Installation using pip
```
pip install bb_cleanup
```
# Building from Sources
```
python -m build
pip install .\dist\bb_cleanup-0.1.31-py3-none-any.whl
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
