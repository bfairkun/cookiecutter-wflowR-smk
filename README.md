# cookiecutter-snakemake-workflow

Cookiecutter template for snakemake workflows.

Install cookiecutter:
```
pip install cookiecutter
```

Start creating a snakemake-workflow from cookiecutter:
```
cookiecutter https://github.com/bfairkun/cookiecutter-wflowR-smk.git
```

Start scripting workflow.

Insert your code into the respective folders, i.e. `scripts`, `rules`, and `envs`. Define the entry point of the workflow in the `Snakefile` and the main configuration in the `config.yaml` file. and cluster configuration in `cluster-config.json`.

Make tests in `.tests` folder.
