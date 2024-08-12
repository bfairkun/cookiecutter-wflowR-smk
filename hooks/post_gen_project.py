#!/usr/bin/env python

"""
Post cookiecutter hook script to generate a conda environment for snakemake and initialize git repos with submodules
"""

import sys
import os
import distutils.spawn
import subprocess
import collections

def FindCondaExecutable():
    """
    return either 'mamba', 'conda', or None depending on which executables are available
    """
    if distutils.spawn.find_executable('mamba'):
        return('mamba')
    elif distutils.spawn.find_executable('conda'):
        return('conda')
    else:
        return(None)

# Load the context from cookiecutter.json
submodules = eval("{{ cookiecutter.submodules }}", {"OrderedDict": collections.OrderedDict})

# Initialize a git repository in the project directory
subprocess.run(["git", "init"], check=True)

# Add each submodule
for submodule_name, remote_url in submodules.items():
    submodule_dest = "code/module_workflows/" + submodule_name
    subprocess.run(["git", "submodule", "add", remote_url, submodule_dest], check=True)

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
