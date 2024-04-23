# Databricks notebook source
# MAGIC %md
# MAGIC >Creating external tables in the bronze layer
# MAGIC * Need to import two jsons :
# MAGIC 1. driver.json and 
# MAGIC 2. results.json

# COMMAND ----------

# MAGIC %sql
# MAGIC drop table if exists formulaOne_dev.bronze.drivers;
# MAGIC
# MAGIC create table if not exists formulaOne_dev.bronze.drivers
# MAGIC (
# MAGIC   driverId int,
# MAGIC   driverRef string,
# MAGIC   number int,
# MAGIC   code string,
# MAGIC   name struct<forename : string, surname : string>,
# MAGIC   dob date,
# MAGIC   nationality string,
# MAGIC   url string
# MAGIC )
# MAGIC using json 
# MAGIC options (path "abfss://bronze@maxdev0unity0extstorage.dfs.core.windows.net/drivers.json");

# COMMAND ----------

# MAGIC %sql
# MAGIC drop table if exists formulaOne_dev.bronze.results;
# MAGIC
# MAGIC create table if not exists formulaOne_dev.bronze.results
# MAGIC (
# MAGIC   resultId int,
# MAGIC   raceId int,
# MAGIC   driverId int,
# MAGIC   constructorId int,
# MAGIC   number int,
# MAGIC   grid int,
# MAGIC   position int,
# MAGIC   positionText string,
# MAGIC   positionOrder int,
# MAGIC   points int,
# MAGIC   laps int,
# MAGIC   time string,
# MAGIC   milliseconds int,
# MAGIC   fastestlap int,
# MAGIC   fastestLapTime string,
# MAGIC   fastestLapSpeed float,
# MAGIC   statusId string
# MAGIC )
# MAGIC using json 
# MAGIC options (path "abfss://bronze@maxdev0unity0extstorage.dfs.core.windows.net/results.json");

# COMMAND ----------


