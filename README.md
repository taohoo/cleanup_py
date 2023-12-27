# cleanup
Match and clean files using Unix shell style wildcards.
# Installing with pip
```commandline
pip install bb_cleanup
```
# # Installing with building
```
python -m build
pip install .\dist\bb_cleanup-0.1.16-py3-none-any.whl
```
# Command
```
cleanup --help
usage: cleanup [-h] [-d DIR_PATTERNS] [-f FILE_PATTERNS] [-e EXCLUDE_PATTERNS] [config_file]

Clean up the current folder

positional arguments:
  config_file           Configuration file, default to .cleanup in the current working directory

options:
  -h, --help            show this help message and exit
  -d DIR_PATTERNS, --dir_patterns DIR_PATTERNS
                        Matching expressions for folders, using Unix Shell style. If there are multiple expressions, use commas to separate them
  -f FILE_PATTERNS, --file_patterns FILE_PATTERNS
                        Match expressions for files, using Unix Shell style. If there are multiple expressions, use commas to separate them
  -e EXCLUDE_PATTERNS, --exclude_patterns EXCLUDE_PATTERNS
                        Match expressions for files or folders that are not cleaned, using Unix Shell style. If there are multiple expressions, use commas to separate them
```
# Using .clean
```
# Matching expressions for folders, using Unix Shell style. If there are multiple expressions, use commas to separate them
dir_patterns = dist,log,__pycache__,tmp,.pytest_cache
# Match expressions for files, using Unix Shell style. If there are multiple expressions, use commas to separate them
file_patterns = *.pyc
# Match expressions for files or folders that are not cleaned, using Unix Shell style. If there are multiple expressions, use commas to separate them
exclude_patterns = ./venv/*
```
