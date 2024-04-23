# Databricks notebook source
# MAGIC %md
# MAGIC >Creating managed tables in silver schema
# MAGIC
# MAGIC 1. drivers
# MAGIC 2. results

# COMMAND ----------

# MAGIC %sql
# MAGIC create table if not exists formulaOne_dev.silver.drivers
# MAGIC as 
# MAGIC (
# MAGIC select driverId as driver_id,
# MAGIC       driverRef as driver_ref,
# MAGIC       number,
# MAGIC       code,
# MAGIC       concat(name.forename,' ',name.surname) as name,
# MAGIC       dob,
# MAGIC       nationality,
# MAGIC       current_timestamp() as ingestion_date
# MAGIC       from formulaOne_dev.bronze.drivers
# MAGIC );

# COMMAND ----------

# MAGIC %sql
# MAGIC create table if not exists formulaOne_dev.silver.results
# MAGIC as 
# MAGIC (
# MAGIC select 
# MAGIC       resultId as result_id,
# MAGIC raceId as race_id,
# MAGIC driverId as driver_id,
# MAGIC constructorId as constructor_id,
# MAGIC number,
# MAGIC grid,
# MAGIC position,
# MAGIC positionText as position_text,
# MAGIC positionOrder as position_order,
# MAGIC points,
# MAGIC laps,
# MAGIC time,
# MAGIC milliseconds,
# MAGIC fastestlap as fastest_lap,
# MAGIC fastestLapTime as fastest_lap_time,
# MAGIC fastestLapSpeed as fastest_lap_speed,
# MAGIC statusId as status_id,
# MAGIC current_timestamp() as ingestion_date 
# MAGIC       from formulaOne_dev.bronze.results
# MAGIC );

# COMMAND ----------


