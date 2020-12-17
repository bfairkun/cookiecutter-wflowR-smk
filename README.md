# cookiecutter-snakemake-workflow

Cookiecutter template for snakemake workflows and [workflowr](https://github.com/jdblischak/workflowr) documentation. This project template is inspired by this [cookiecutter snakemake project template](https://github.com/snakemake-workflows/cookiecutter-snakemake-workflow) and the suggested project structure for [workflowr](https://jdblischak.github.io/workflowr/articles/wflow-01-getting-started.html) R package for creating a static site from Rmarkdown files. I use the project template as follows:

### USAGE

Install cookiecutter:

```
pip install cookiecutter
```

Start creating a snakemake-workflow from cookiecutter:
```
cookiecutter https://github.com/bfairkun/cookiecutter-wflowR-smk.git
```

After filling the prompts, this will create a project template with the following directory structure:

```
.
├── analysis
│   ├── about.Rmd
│   ├── index.Rmd
│   ├── license.Rmd
│   └── _site.yml
├── code
│   ├── cluster-config.json
│   ├── config.yaml
│   ├── envs
│   │   ├── {{\ cookiecutter.repo_name\ }}.yaml
│   │   └── myenv.yaml
│   ├── LICENSE.md
│   ├── README.md
│   ├── rules
│   │   ├── common.smk
│   │   └── other.smk
│   ├── samples.tsv
│   ├── scripts
│   │   └── common
│   │       └── __init__.py
│   ├── Snakefile
│   ├── snakemake_profiles
│   │   └── slurm
│   │       ├── cluster-config.yaml
│   │       ├── config.yaml
│   │       ├── __pycache__
│   │       │   └── slurm_utils.cpython-36.pyc
│   │       ├── slurm-jobscript.sh
│   │       ├── slurm-status.py
│   │       ├── slurm-submit.py
│   │       └── slurm_utils.py
│   └── snakemake.sbatch
├── {{\ cookiecutter.repo_name\ }}.Rproj
├── data
│   └── README.md
├── docs
│   └── assets
├── output
│   └── README.md
├── README.md
└── _workflowr.yml
13 directories, 28 files
```

Start scripting and documenting your project. 

### Guidelines for project organization

- Optionally track the entire project with `git init` in the newly created project root.
- use the `code` directory to create a reproducible snakemake pipeline which does heavy lifting analysis to be run on a cluster environemt from `code` as the working directory. The `code/.gitignore` makes it easy to git track all the code, but ignore tracking the potentially large files in the `code` directory. So as you write the Snakemake pipeline, it is ok to create large untracked files which are too big to push to github. Use the snakemake to do heavy lifting (eg Download NGS data, align, etc) and process the data to small files that can be easily tracked and pushed to github. The cookiecutter will optionally create a conda environment for the snakemake with snakemake and some basic NGS processing softwares `code/envs/{{ cookiecutter.repo_name }}.yaml` and if you need to create additional rule-specific conda environments for the snakemake, they should  also be saved in `code/envs/`. See the `code/README.md` for more on my snakemake project template.
- Write the snakemake pipeline to output smaller processed files (eg gene x sample count tables for RNA-seq) to `output` where they will be tracked by git.
- Raw data (that should never be directly edited) that is small enough to track with git should go in `data`. 
- Use the `analysis` directory to write Rmarkdown files which you want to use to document your thoughts and analysis of processed data. If these Rmd files read in the data files in `output` or `data` it should be easy for anyone to edit or re-run your Rmd files by cloning this repo (without needing to run the snakemake or do the computationally intensive things)
- Use the [workflowr](https://jdblischak.github.io/workflowr/index.html) R package  to render all the Rmd files in `analysis` into html in the `docs` folder (`workflowr::wflow_build()` function). Use github's free hosting of static sites to share the `docs` website. The `docs/assets` might be useful to save images that can reference in the site.
- Occasionally I write Rmd files that need access to the large untracked files output by the Snakemake. In this case, it is nice to follow a naming convention to specify which Rmd files need access to these large files.
