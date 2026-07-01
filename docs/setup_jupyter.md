# Jupyter Setup

This project has its own local Python environment in `.venv`.

## Activate the Environment

From `C:\.projects\ab-testing`:

```powershell
.\.venv\Scripts\Activate.ps1
```

## Start JupyterLab

Option 1, use the helper script:

```powershell
.\scripts\start_jupyter.ps1
```

Option 2, run Jupyter directly:

```powershell
.\.venv\Scripts\jupyter-lab.exe
```

The helper script also sets project-local Jupyter and IPython folders under `.jupyter/` and `.ipython/`.

## Kernel

The project venv is registered as:

```text
Python (ab-testing)
```

When opening notebooks, choose that kernel.

The helper scripts also create a local kernel spec that points directly at `.venv\Scripts\python.exe`.

## Reinstall Dependencies

If the environment ever needs to be rebuilt:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Then launch Jupyter with `.\scripts\start_jupyter.ps1`. The script will recreate the local kernel spec.

## Execute a Notebook

To rerun a notebook from the command line:

```powershell
.\scripts\execute_notebook.ps1 notebooks\01_data_audit.ipynb
```
