# Databricks notebook source
# MAGIC %md
# MAGIC ### Explore DBFS Root
# MAGIC 1. List all the folder in DBFS root
# MAGIC 2. Interact with DBFS File Browser
# MAGIC 3. Upload file to DBFS root

# COMMAND ----------

display(dbutils.fs.ls('/'))

# COMMAND ----------

display(dbutils.fs.ls('/FileStore'))

# COMMAND ----------

display(spark.read.csv('dbfs:/FileStore/circuits.csv'))