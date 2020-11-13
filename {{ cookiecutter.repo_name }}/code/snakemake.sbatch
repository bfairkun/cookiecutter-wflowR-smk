#!/bin/bash

# sbatch submission script to run main snakemake process. It then submits
# individual jobs from the compute node.

#SBATCH --job-name=snakemake
#SBATCH --output=snakemake.sbatch.log
#SBATCH --time=1-08:00:00
#SBATCH --partition=broadwl
#SBATCH --mem=4G
#SBATCH --tasks-per-node=4


snakemake --profile snakemake_profiles/slurm
