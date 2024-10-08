#!/usr/bin/env python

"""
Pre cookiecutter hook script to check that some template variables are valid. Specifically, no weird characters in the repo_name, only and only word characters [a-zA-Z0-9_] in module names.
"""

import re
import sys
import collections


REPO_REGEX = r'^[_a-zA-Z\-0-9]+$'

repo_name = '{{ cookiecutter.repo_name }}'

if not re.match(REPO_REGEX, repo_name):
    print('ERROR: %s is not a valid name for repo_name' % repo_name)
    # exits with status 1 to indicate failure
    sys.exit(1)

submodules = eval("{{ cookiecutter.submodules }}", {"OrderedDict": collections.OrderedDict})

for submodule in submodules.keys():
    if not re.match(r'^\w+$', submodule):
        print('ERROR: %s is not a valid name for repo_name' % submodule)
        sys.exit(1)

