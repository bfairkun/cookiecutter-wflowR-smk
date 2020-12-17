#!/usr/bin/env python

"""
Post cookiecutter hook script to generate a conda environment for snakemake
"""

import sys
import os
import distutils.spawn

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
