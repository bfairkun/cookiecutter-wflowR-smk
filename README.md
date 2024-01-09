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
{{\ cookiecutter.repo_name\ }}/
├── analysis
│   ├── about.Rmd
│   ├── index.Rmd
│   ├── license.Rmd
│   └── _site.yml
├── code
│   ├── config
│   │   ├── config.yaml
│   │   └── samples.tsv
│   ├── envs
│   │   ├── {{\ cookiecutter.repo_name\ }}.yaml
│   │   ├── jupyter.yml
│   │   ├── myenv.yaml
│   │   └── r_essentials.yml
│   ├── module_workflows
│   ├── README.md
│   ├── rules
│   │   ├── common.smk
│   │   └── other.smk
│   ├── scripts
│   │   └── common
│   │       └── __init__.py
│   ├── Snakefile
│   └── snakemake_profiles
│       └── slurm
│           ├── cluster-config.yaml
│           ├── config.yaml
│           ├── slurm-jobscript.sh
│           ├── slurm-status.py
│           ├── slurm-submit.py
│           └── slurm_utils.py
├── {{\ cookiecutter.repo_name\ }}.Rproj
├── data
│   └── README.md
├── docs
│   └── assets
├── output
│   └── README.md
├── README.md
└── _workflowr.yml

14 directories, 26 files
```
Start scripting and documenting your project. 

### Guidelines for project organization

- Optionally track the entire project with `git init` in the newly created project root.
- use the `code` directory to create a reproducible snakemake pipeline which does heavy lifting analysis to be run on a cluster environemt from `code` as the working directory. The `code/.gitignore` makes it easy to git track all the code, but ignore tracking the potentially large files in the `code` directory. So as you write the Snakemake pipeline, it is ok to create large untracked files which are too big to push to github. Use the snakemake to do heavy lifting (eg Download NGS data, align, etc) and process the data to small files that can be easily tracked and pushed to github. The cookiecutter will optionally create a conda environment for the snakemake with snakemake and some basic NGS processing softwares `code/envs/{{ cookiecutter.repo_name }}.yaml` and if you need to create additional rule-specific conda environments for the snakemake, they should  also be saved in `code/envs/`. Using [snakemake modules](https://snakemake.readthedocs.io/en/stable/snakefiles/modularization.html#modules) is a nice way to start a workflow, as in [this example](https://github.com/bfairkun/sm_splicingmodulators/blob/265a0f233c26c10c75e5ca923d94400daa7e40b3/code/Snakefile#L8-L19) where I can include the code for a submodule as a nested git submodule. See the `code/README.md` for more on my snakemake project template.
- Write the snakemake pipeline to output smaller processed files (eg gene x sample count tables for RNA-seq) to `output` where they will be tracked by git.
- Raw data (that should never be directly edited) that is small enough to track with git should go in `data`. 
- Use the `analysis` directory to write Rmarkdown (`.Rmd`) and jupyter notebook (`.ipynb`) files which you want to use to document your thoughts and analysis of processed data. If these notebook files only read in the data files in git tracked in `output` or `data` it should be easy for anyone to edit or re-run your notebooks by cloning this repo (without needing to run the snakemake or do the computationally intensive things)
    - To render notebooks into a static site and host on github, render Rmarkdowns files into html and place into `docs`. ipynb files are automatically rendered by github, so it is not necessary to render them to html. For Rmarkdown, one nice way to render them is using the [workflowr](https://jdblischak.github.io/workflowr/index.html) R package. The tree of this project is basically the same as demonstrated in the [workflowr vignette](https://cran.r-project.org/web/packages/workflowr/vignettes/wflow-01-getting-started.html) after running `workflowr::wflow_start`. So note the presence of some files already populated in `analysis` (eg `analysis/index.html`, `analysis/_site.yaml`) that can be rendered to html for a nice skeleton site. The `workflowr::wflow_build()` function conveniently will render Rmd files to html and place the html in the `docs` folder. The `docs/assets` might be useful to save images that can also be reference in notebooks and their rendered htmls. To enable github web hosting, be sure to add project to github, and modify the project settings on github to build a site from the `/docs` folder (in the "Pages" section of project settings).
    - Occasionally I write notebooks that need access to the large untracked files output by the Snakemake. In this case, it is nice to follow a naming convention to specify which notebooks need access to these large files, so it is clear what notebooks can be run simply by cloning the repo, versus needing access to large untracked files.
