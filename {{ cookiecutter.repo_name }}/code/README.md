# Snakemake workflow: {{cookiecutter.project_name}}

[![Snakemake](https://img.shields.io/badge/snakemake-≥{{cookiecutter.min_snakemake_version}}-brightgreen.svg)](https://snakemake.bitbucket.io)
[![Build Status](https://travis-ci.org/snakemake-workflows/{{cookiecutter.repo_name}}.svg?branch=master)](https://travis-ci.org/snakemake-workflows/{{cookiecutter.repo_name}})


## Authors

* {{cookiecutter.full_name}} (@{{cookiecutter.username}})

## Usage

### Step 1: Install workflow

If you simply want to use this workflow, clone the [latest release](https://github.com/bfairkun/{{cookiecutter.repo_name}}).
If you intend to modify and further develop this workflow, fork this repository. Please consider providing any generally applicable modifications via a pull request.

### Step 2: Configure workflow

Configure the workflow according to your needs via editing the file `config.yaml`. Configure cluster settings in `cluster-config.json` or use/modify the config yaml files in the `snakemake_profiles/slurm/` profile to run on UChicago RCC Midway.

### Step 3: Execute workflow

Test your configuration by performing a dry-run via

    snakemake -n

Execute the workflow locally via

    snakemake --cores $N

using `$N` cores or run it in a cluster environment via

    snakemake --profile snakemake_profiles/slurm

or by executing the included sbatch script to execute the snakemake process from a cluster

    sbatch snakemake.sbatch

This is the option I usually do, and it will output snakemake log to `snakemake.sbatch.log``

See the [Snakemake documentation](https://snakemake.readthedocs.io) for further details.
