# Databricks notebook source
# MAGIC %md
# MAGIC >Creating catalog and schemas required
# MAGIC 1. Catalog (without managed location).
# MAGIC 2. Schemas (with managed location).
# MAGIC
# MAGIC - We are not using managed location for catalog since we are already defining it while creating schemas.

# COMMAND ----------

# MAGIC %sql
# MAGIC create catalog if not exists formulaOne_dev;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC -- bronze
# MAGIC create schema if not exists formulaOne_dev.bronze
# MAGIC managed location 'abfss://bronze@maxdev0unity0extstorage.dfs.core.windows.net/';
# MAGIC -- silver
# MAGIC create schema if not exists formulaOne_dev.silver
# MAGIC managed location 'abfss://silver@maxdev0unity0extstorage.dfs.core.windows.net/';
# MAGIC -- gold
# MAGIC create schema if not exists formulaOne_dev.gold
# MAGIC managed location 'abfss://gold@maxdev0unity0extstorage.dfs.core.windows.net/';

# COMMAND ----------


