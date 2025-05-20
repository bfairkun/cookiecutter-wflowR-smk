#!/usr/bin/env python

"""
Post cookiecutter hook script to generate a conda environment for snakemake and initialize git repos with submodules
"""

import sys
import os
import subprocess
import collections
import shutil

def FindCondaExecutable():
    """
    Return either 'mamba', 'conda', or None depending on which executables are available.
    """
    if shutil.which('mamba'):
        return 'mamba'
    elif shutil.which('conda'):
        return 'conda'
    else:
        return None

# Load the context from cookiecutter.json
submodules = eval("{{ cookiecutter.submodules }}", {"OrderedDict": collections.OrderedDict})

# Initialize a git repository in the project directory
subprocess.run(["git", "init"], check=True)

# Add each submodule, supporting extra arguments like branch
for submodule_name, submodule_info in submodules.items():
    if isinstance(submodule_info, dict):
        remote_url = submodule_info.get("url")
        branch = submodule_info.get("branch")
    else:
        remote_url = submodule_info
        branch = None
    submodule_dest = "code/module_workflows/" + submodule_name
    cmd = ["git", "submodule", "add"]
    if branch:
        cmd += ["-b", branch]
    cmd += [remote_url, submodule_dest]
    subprocess.run(cmd, check=True)

# Update the submodules
subprocess.run(["git", "submodule", "update", "--init", "--recursive"], check=True)

print("Git repository initialized and submodules (if provided) added successfully.")


# Make conda env
make_conda_env = '{{ cookiecutter.make_conda_env }}'
if make_conda_env == 'y':
    conda_executable = FindCondaExecutable()
    if not conda_executable:
        print('ERROR: could not find conda executable' % make_conda_env)
        sys.exit(1)
    print("Attempting to create conda environment from code/envs/{{ cookiecutter.repo_name }}.yaml")
    sys.exit(
            os.system("%s env create -f code/envs/{{ cookiecutter.repo_name }}.yaml" %conda_executable)
            )
elif make_conda_env =='n':
    pass
else:
    print('ERROR: %s is not a valid option for make_conda_env' % make_conda_env)
    # exits with status 1 to indicate failure
    sys.exit(1)
