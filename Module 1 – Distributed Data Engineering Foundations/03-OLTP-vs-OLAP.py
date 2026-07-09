# Databricks notebook source
# COMMAND ----------
# MAGIC %md
# MAGIC # Enterprise Data Engineering & Agentic AI Mastery (2026)
# MAGIC ## Module 1 - Notebook 03
# MAGIC # OLTP vs OLAP

# COMMAND ----------
# MAGIC %md
# MAGIC ## Learning Objectives
# MAGIC - Understand OLTP and OLAP
# MAGIC - Compare transactional and analytical systems
# MAGIC - Learn row vs column storage
# MAGIC - Connect OLTP to Lakehouse and AI

# COMMAND ----------
# MAGIC %md
# MAGIC ## Enterprise Story
# MAGIC An e-commerce platform uses OLTP databases for customer orders and an OLAP platform for dashboards, forecasting and AI.

# COMMAND ----------
# MAGIC %md
# MAGIC ## OLTP vs OLAP Comparison
# MAGIC | Attribute | OLTP | OLAP |
# MAGIC |---|---|---|
# MAGIC | Workload | Transactions | Analytics |
# MAGIC | Storage | Row | Column |
# MAGIC | Schema | Normalized | Star/Snowflake |
# MAGIC | Users | Operational | Business |

# COMMAND ----------
# MAGIC %md
# MAGIC ## Architecture
# MAGIC ```mermaid
# MAGIC flowchart LR
# MAGIC A[Applications]-->B[(OLTP)]-->C[CDC]-->D[Lakehouse]-->E[BI] 
# MAGIC D-->F[AI]
# MAGIC ```

# COMMAND ----------
orders=[(1,101,'Laptop',85000),(2,102,'Mouse',1200),(3,101,'Keyboard',3200)]
df=spark.createDataFrame(orders,['order_id','customer_id','product','amount'])
display(df)

# COMMAND ----------
from pyspark.sql.functions import sum
display(df.groupBy('customer_id').agg(sum('amount').alias('revenue')))

# COMMAND ----------
df.createOrReplaceTempView('orders')

# COMMAND ----------
# MAGIC %sql
# MAGIC SELECT customer_id,SUM(amount) revenue FROM orders GROUP BY customer_id ORDER BY revenue DESC;

# COMMAND ----------
# MAGIC %md
# MAGIC ## AI Perspective
# MAGIC Enterprise AI, RAG and Agentic AI consume curated analytical data, not live OLTP databases.

# COMMAND ----------
# MAGIC %md
# MAGIC ## Interview Questions
# MAGIC - Why separate OLTP and OLAP?
# MAGIC - Why is columnar storage faster for analytics?
# MAGIC - Explain CDC from OLTP to Lakehouse.

# COMMAND ----------
# MAGIC %md
# MAGIC ## Assignment
# MAGIC Generate 100000 synthetic orders and identify top customers.

# COMMAND ----------
# MAGIC %md
# MAGIC ## Summary
# MAGIC OLTP runs the business. OLAP analyzes the business. Lakehouse connects both for BI and AI.
