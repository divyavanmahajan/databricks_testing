# Unit testing in Databricks
Author: Divya van Mahajan


## Instructions to use this repo.

- Read Unit Testing in Databricks as explained in https://learn.microsoft.com/en-us/azure/databricks/notebooks/testing 
- Fork this repo.
- Create a Databricks Repo with your forked repo
- **For Python testing**
- Run the notebook "python/setup_db" and attach it to a cluster. (Cluster should not be a shared cluster).
- Run the notebook "python/function_nb" to test the functions defined in myfunctions.py
- Run the notebook "python/testing_nb" to run Pytest for the tests defined in test_myfunctions.py
- **For Scala testing**
- Run the notebook "scala/test_myfunctions" to run the tests.
  


## Organize functions and unit tests
There are a few common approaches for organizing your functions and their unit tests with notebooks. Each approach has its benefits and challenges.
For Python, R, and Scala notebooks, common approaches include the following:
### Store functions and their unit tests outside of notebooks..
Benefits: You can call these functions with and outside of notebooks. Test frameworks are better designed to run tests outside of notebooks.
Challenges: This approach is not supported for Scala notebooks. This approach requires Databricks Repos. This approach also increases the number of files to track and maintain.
### Store functions in one notebook and their unit tests in a separate notebook..
Benefits: These functions are easier to reuse across notebooks.
Challenges: The number of notebooks to track and maintain increases. These functions cannot be used outside of notebooks. These functions can also be more difficult to test outside of notebooks.
### Store functions and their unit tests within the same notebook..
Benefits: Functions and their unit tests are stored within a single notebook for easier tracking and maintenance.
Challenges: These functions can be more difficult to reuse across notebooks. These functions cannot be used outside of notebooks. These functions can also be more difficult to test outside of notebooks.

For Python and R notebooks, Databricks recommends storing functions and their unit tests outside of notebooks. For Scala notebooks, Databricks recommends including functions in one notebook and their unit tests in a separate notebook.
For SQL notebooks, Databricks recommends that you store functions as SQL user-defined functions (SQL UDFs) in your schemas (also known as databases). You can then call these SQL UDFs and their unit tests from SQL notebooks.
