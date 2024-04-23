# Databricks notebook source
# MAGIC %md
# MAGIC >Creating managed tables in gold schema

# COMMAND ----------

# MAGIC %sql
# MAGIC drop table if exists formulaOne_dev.gold.driver_wins;
# MAGIC
# MAGIC create table formulaOne_dev.gold.driver_wins as(
# MAGIC select d.name, count(1) as number_of_wins
# MAGIC from formulaOne_dev.silver.drivers d
# MAGIC inner join formulaOne_dev.silver.results r
# MAGIC on d.driver_id = r.driver_id
# MAGIC where r.position = 1
# MAGIC group by d.name
# MAGIC );
# MAGIC
# MAGIC select * from formulaOne_dev.gold.driver_wins order by number_of_wins desc;

# COMMAND ----------


