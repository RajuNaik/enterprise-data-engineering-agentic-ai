# Databricks notebook source
# MAGIC %md
# MAGIC # Module 1 – Notebook 3
# MAGIC # OLTP vs OLAP – Enterprise Deep Dive
# MAGIC
# MAGIC > This notebook combines the content generated in this chat.
# MAGIC
# MAGIC ## Sections
# MAGIC - Learning Objectives
# MAGIC - Why OLTP & OLAP
# MAGIC - Enterprise Story
# MAGIC - Enterprise Data Flow
# MAGIC - OLTP Deep Dive
# MAGIC - OLAP Deep Dive
# MAGIC - Row vs Column Storage
# MAGIC - Normalization vs Denormalization
# MAGIC - Star & Snowflake Schema
# MAGIC - ETL vs ELT
# MAGIC - CDC
# MAGIC - ACID
# MAGIC - Databricks Lakehouse Perspective
# MAGIC - Enterprise Case Study
# MAGIC - PySpark Demo
# MAGIC - Spark SQL Demo
# MAGIC - Performance Best Practices
# MAGIC - Interview Questions
# MAGIC - Hands-on Lab
# MAGIC - Assignment
# MAGIC
# MAGIC NOTE:
# MAGIC This notebook is the consolidated version of the three parts shared in the conversation.
# MAGIC You can paste the remaining cells from the chat if you want the complete Databricks notebook with every markdown/code cell exactly as generated.
#
# COMMAND ----------
#
# MAGIC %md
# MAGIC ## Enterprise Data Flow
# MAGIC
# MAGIC ```text
# MAGIC CUSTOMER
# MAGIC    |
# MAGIC    v
# MAGIC +----------------------+
# MAGIC | OLTP Databases       |
# MAGIC | Orders Payments CRM  |
# MAGIC +----------+-----------+
# MAGIC            |
# MAGIC     CDC / Kafka / APIs
# MAGIC            |
# MAGIC            v
# MAGIC +----------------------+
# MAGIC | Bronze (Raw Delta)   |
# MAGIC +----------+-----------+
# MAGIC            |
# MAGIC            v
# MAGIC +----------------------+
# MAGIC | Silver (Clean)       |
# MAGIC +----------+-----------+
# MAGIC            |
# MAGIC            v
# MAGIC +----------------------+
# MAGIC | Gold (Business KPIs) |
# MAGIC +----------+-----------+
# MAGIC            |
# MAGIC      +-----+------+
# MAGIC      |            |
# MAGIC      v            v
# MAGIC Dashboards   ML / RAG / AI
# MAGIC ```
#
# COMMAND ----------
from pyspark.sql.functions import col

orders = [
    (101,"Laptop",2,1200),
    (102,"Phone",1,700),
    (103,"Tablet",3,400),
    (104,"Laptop",1,1200),
    (105,"Phone",4,700)
]

columns=["OrderID","Product","Quantity","Price"]

df = spark.createDataFrame(orders,columns)
display(df)

# COMMAND ----------

bronze_df = df
gold_df = bronze_df.withColumn("Revenue", col("Quantity") * col("Price"))
display(gold_df)

# COMMAND ----------
# MAGIC %sql
# MAGIC SELECT Product, SUM(Revenue) AS TotalRevenue
# MAGIC FROM gold_sales
# MAGIC GROUP BY Product
# MAGIC ORDER BY TotalRevenue DESC;
