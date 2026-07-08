# Databricks notebook source
# COMMAND ----------
# MAGIC %md
# MAGIC <div style="background:#0F172A;color:white;padding:20px;border-radius:12px">
# MAGIC <h1>Enterprise Data Engineering & Agentic AI (2026 Edition)</h1>
# MAGIC <h2>Module 1 • Data Engineering Fundamentals</h2>
# MAGIC <p><b>Notebook Version:</b> Premium v1</p>
# MAGIC </div>

# COMMAND ----------
# MAGIC %md
# MAGIC ## Learning Objectives
# MAGIC 
# MAGIC - Understand Data Engineering from first principles
# MAGIC - Learn enterprise data lifecycle
# MAGIC - Build first Spark transformations
# MAGIC - Understand why AI depends on Data Engineering

# COMMAND ----------
# MAGIC %md
# MAGIC ## Enterprise Story
# MAGIC 
# MAGIC Imagine joining a Fortune 100 company. Hundreds of systems generate data every second. Reports disagree, AI hallucinates because enterprise knowledge is inconsistent. Your first mission is to build a trustworthy data platform.

# COMMAND ----------
# MAGIC %md
# MAGIC ## Why Data Engineering Exists
# MAGIC 
# MAGIC Applications are optimized to run businesses—not answer analytical questions. Data Engineering bridges operational systems and decision making.

# COMMAND ----------
# MAGIC %md
# MAGIC ## Definition
# MAGIC 
# MAGIC Data Engineering is the discipline of designing, building, operating and governing systems that ingest, transform, validate, store and serve data for analytics, ML and AI.

# COMMAND ----------
# MAGIC %md
# MAGIC ## Evolution
# MAGIC 
# MAGIC Excel → Databases → Data Warehouse → Hadoop → Data Lake → Lakehouse → Enterprise AI Platform

# COMMAND ----------
# MAGIC %md
# MAGIC ## Modern Lifecycle
# MAGIC 
# MAGIC ```mermaid
# MAGIC flowchart LR
# MAGIC A[Sources]-->B[Ingestion]-->C[Storage]-->D[Transformation]-->E[Quality]-->F[Governance]-->G[Lakehouse]-->H[BI / ML / RAG / Agents]
# MAGIC ```

# COMMAND ----------
# MAGIC %md
# MAGIC ## Core Responsibilities
# MAGIC 
# MAGIC • Data ingestion
# MAGIC • Batch & Streaming
# MAGIC • Modeling
# MAGIC • Quality
# MAGIC • Governance
# MAGIC • Performance
# MAGIC • Security
# MAGIC • Cost optimization

# COMMAND ----------
# MAGIC %md
# MAGIC ## Enterprise Example
# MAGIC 
# MAGIC Retail example: POS, ERP, CRM, IoT, E-commerce and supplier feeds converge into a Lakehouse powering dashboards, forecasting and AI assistants.

# COMMAND ----------
# MAGIC %md
# MAGIC ## AI Perspective
# MAGIC 
# MAGIC LLMs require governed enterprise knowledge. Data Engineering prepares documents, tables, metadata, embeddings and continuous refresh pipelines.

# COMMAND ----------
# MAGIC %md
# MAGIC ## Best Practices
# MAGIC 
# MAGIC Treat data as a product. Automate validation. Version schemas. Monitor pipelines. Build idempotent workflows.

# COMMAND ----------
# MAGIC %md
# MAGIC ## Common Mistakes
# MAGIC 
# MAGIC Hard-coded paths, no quality checks, tiny files, collecting large DataFrames to driver, missing lineage.

# COMMAND ----------
# MAGIC %md
# MAGIC ## Lab 1 – Create Sample Dataset

# COMMAND ----------
products=[
(1,"Laptop","Electronics",80000),
(2,"Mouse","Electronics",500),
(3,"Keyboard","Electronics",2500),
(4,"Monitor","Electronics",18000),
(5,"Chair","Furniture",7000)
]
df=spark.createDataFrame(products,["product_id","product_name","category","price"])
display(df)

# COMMAND ----------
# MAGIC %md
# MAGIC ## Lab 2 – Basic Transformations

# COMMAND ----------
from pyspark.sql.functions import col,avg,sum,count
display(df.filter(col("price")>5000))
# COMMAND ----------
display(df.groupBy("category").agg(
count("*").alias("products"),
avg("price").alias("avg_price"),
sum("price").alias("total_price")
))
# COMMAND ----------
# MAGIC %md
# MAGIC ## Lab 3 – SQL

# COMMAND ----------
df.createOrReplaceTempView("products")
# COMMAND ----------
# MAGIC %sql
# MAGIC SELECT category,
# MAGIC COUNT(*) products,
# MAGIC ROUND(AVG(price),2) avg_price,
# MAGIC SUM(price) total_price
# MAGIC FROM products
# MAGIC GROUP BY category
# MAGIC ORDER BY total_price DESC;
# COMMAND ----------
# MAGIC %md
# MAGIC ## Lab 4 – Delta Lake

# COMMAND ----------
df.write.mode("overwrite").format("delta").save("/tmp/de_handbook/products")
display(spark.read.format("delta").load("/tmp/de_handbook/products"))
# COMMAND ----------
# MAGIC %md
# MAGIC ## Knowledge Check
# MAGIC 
# MAGIC 1. Why can't AI succeed without Data Engineering?
# MAGIC 2. Difference between operational and analytical systems?
# MAGIC 3. Why use Delta instead of CSV?

# COMMAND ----------
# MAGIC %md
# MAGIC ## Interview Corner
# MAGIC 
# MAGIC ### Beginner
# MAGIC - What is Data Engineering?
# MAGIC - Responsibilities?
# MAGIC 
# MAGIC ### Intermediate
# MAGIC - Explain a modern data platform.
# MAGIC 
# MAGIC ### Senior
# MAGIC - Design an ingestion platform for 100 TB/day.
# MAGIC - How would you ensure data quality and governance?

# COMMAND ----------
# MAGIC %md
# MAGIC ## Assignment
# MAGIC 
# MAGIC 1. Generate 1 million rows using `spark.range()`.
# MAGIC 2. Create a `sales_amount` column.
# MAGIC 3. Aggregate by modulo bucket.
# MAGIC 4. Save as Delta.
# MAGIC 5. Query using SQL.
# MAGIC 6. Explain the physical plan.

# COMMAND ----------
large_df=(spark.range(1000000)
.withColumn("bucket",(col("id")%10))
.withColumn("sales_amount",col("id")*2))
display(large_df.limit(10))
# COMMAND ----------
# MAGIC %md
# MAGIC ## Summary
# MAGIC 
# MAGIC Data Engineering is the foundation for Analytics, Machine Learning, Enterprise RAG and Agentic AI. Every topic in this course builds on this foundation.
# MAGIC 
# MAGIC **Next Notebook:** Distributed Computing

