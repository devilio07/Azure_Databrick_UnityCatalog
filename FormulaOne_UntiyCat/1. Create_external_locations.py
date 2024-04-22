# Databricks notebook source
# MAGIC %md
# MAGIC >Creating external location using Storage Credential using SQL <br>
# MAGIC ##### Layers :
# MAGIC 1. Bronze
# MAGIC 2. Silver
# MAGIC 3. Gold

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Bronze
# MAGIC create external location if not exists maxdev_unity_ext_bronze
# MAGIC url 'abfss://bronze@maxdev0unity0extstorage.dfs.core.windows.net/'
# MAGIC with (storage credential maxdev_unity_ext_storage);
# MAGIC -- -- Silver
# MAGIC create external location if not exists maxdev_unity_ext_silver
# MAGIC url 'abfss://silver@maxdev0unity0extstorage.dfs.core.windows.net/'
# MAGIC with (storage credential maxdev_unity_ext_storage);
# MAGIC -- -- Gold
# MAGIC create external location if not exists maxdev_unity_ext_gold
# MAGIC url 'abfss://gold@maxdev0unity0extstorage.dfs.core.windows.net/'
# MAGIC with (storage credential maxdev_unity_ext_storage);
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC desc external location maxdev_unity_ext_bronze;

# COMMAND ----------

# MAGIC %fs
# MAGIC
# MAGIC ls 'abfss://bronze@maxdev0unity0extstorage.dfs.core.windows.net/'

# COMMAND ----------


