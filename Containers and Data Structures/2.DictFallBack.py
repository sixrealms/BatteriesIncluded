'''When working with config values, its common to look them up in multiple places
This can lead to multiple if statements. ChainMap accepts multiple dicts and looks up the values'''
import os

command_line_options = None  # just for demo
config_file_options = None  # just for demo

value = command_line_options.get('optname')
if value is None:
    value = os.environ.get('optname')
if value is None:
    value = config_file_options.get('optname')
if value is None:
    value = 'default-value'

# Alternative is to use collections.ChainMap

import os
from collections import ChainMap

options = ChainMap(command_line_options, os.environ, config_file_options)
value = options.get('optname', 'default-value')

print(value)
