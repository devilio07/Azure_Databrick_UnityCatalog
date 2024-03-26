-- Databricks notebook source
select * from demo_catalog.demo_schema.circuits;

-- COMMAND ----------

describe table extended demo_catalog.demo_schema.circuits;

-- COMMAND ----------

use catalog demo_catalog;
select current_catalog();

-- COMMAND ----------

use schema demo_schema;
show schemas;

-- COMMAND ----------

select * from circuits;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### Accessing Table data using python.

-- COMMAND ----------

-- MAGIC %python
-- MAGIC
-- MAGIC df_circuits = spark.table('demo_catalog.demo_schema.circuits')
-- MAGIC display(df_circuits)

-- COMMAND ----------


