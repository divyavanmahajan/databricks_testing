# Databricks notebook source
# MAGIC %pip install pytest
# MAGIC dbutils.library.restartPython()

# COMMAND ----------

#importing required libraries
import pytest
import os
import sys

# Get the path to this notebook to determine repo root
notebook_path = dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get()

# Get the repo's root directory name.
repo_root = os.path.dirname(os.path.dirname(notebook_path))

# Prepare to run pytest from the repo.
os.chdir(f"/Workspace/{repo_root}/python")

# Using sys to skip writing pyc files on a readonly filesystem.
sys.dont_write_bytecode = True

# Run pytest.
retcode = pytest.main([".", "-v", "-p", "no:cacheprovider"])

# Assert if tests have passed or failed
assert retcode == 0, "The pytest invocation failed. See stderr for details."


# COMMAND ----------


