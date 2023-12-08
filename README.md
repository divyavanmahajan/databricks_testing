# Unit testing in Databricks
Author: Divya van Mahajan

Testing in Databricks as explained in https://learn.microsoft.com/en-us/azure/databricks/notebooks/testing 

To use

- Fork this repo.
- Create a Databricks Repo with your forked repo
- Run the notebook "python/setup_db" and attach it to a cluster. (Cluster should not be a shared cluster).
- Run the notebook "python/function_nb" to test the functions defined in myfunctions.py
- Run the notebook "python/testing_nb" to run Pytest for the tests defined in test_myfunctions.py

