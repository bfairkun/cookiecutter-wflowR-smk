import pandas as pd
import os


# try/except useful for running this script in isolation in interactive shell
# for debugging
try:
    samples = pd.read_csv(config["samples"],sep='\t', index_col=0)
except (NameError, KeyError) as NameOrKeyError:
    samples = pd.read_csv("config/samples.tsv",sep='\t', index_col=0)

# Add code for function definitions and other things that must be defined prior
# to rest of workflow (eg custom snakemake input functions)
