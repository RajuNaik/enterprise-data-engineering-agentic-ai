# Databricks notebook source
# MAGIC %md
# MAGIC <div style="background:#0F172A;color:white;padding:18px;border-radius:10px">
# MAGIC <h1>Enterprise Data Engineering & Agentic AI (2026 Edition)</h1>
# MAGIC <h2>Module 1 – Distributed Data Engineering Foundations</h2>
# MAGIC <h2>Topic 1 – Data Engineering Fundamentals</h2>
# MAGIC <p><b>Duration:</b> 45–60 minutes &nbsp; | &nbsp; <b>Level:</b> Beginner</p>
# MAGIC </div>

# COMMAND ----------

# MAGIC %md
# MAGIC # 🎯 Learning Objectives
# MAGIC By the end of this notebook you will:
# MAGIC - Understand what Data Engineering is.
# MAGIC - Learn why every AI platform depends on Data Engineering.
# MAGIC - Understand the modern enterprise data lifecycle.
# MAGIC - Execute your first PySpark transformations.

# COMMAND ----------

# MAGIC %md
# MAGIC # 🌍 A Story
# MAGIC Imagine joining a global enterprise on Monday morning.
# MAGIC
# MAGIC Your manager says:
# MAGIC - 40+ source systems
# MAGIC - 80 TB of new data every day
# MAGIC - Reports don't match
# MAGIC - AI assistant gives inconsistent answers
# MAGIC
# MAGIC **Question:** Where do you start?
# MAGIC
# MAGIC **Answer:** You first build a reliable Data Engineering platform.

# COMMAND ----------

# MAGIC %md
# MAGIC # 📖 What is Data Engineering?
# MAGIC
# MAGIC **Data Engineering** is the discipline of designing, building and operating systems that ingest, transform, validate, govern and serve data for analytics, machine learning and AI.
# MAGIC
# MAGIC Think of it like a highway system:
# MAGIC - 🚗 Cars = Data
# MAGIC - 🛣️ Roads = Pipelines
# MAGIC - 🚦 Traffic Rules = Governance
# MAGIC - 📍 Destination = BI, ML & AI

# COMMAND ----------

# MAGIC %md
# MAGIC # 🏗️ Enterprise Data Lifecycle
# MAGIC
# MAGIC ```mermaid
# MAGIC flowchart LR
# MAGIC A[Operational Systems]
# MAGIC -->B[Ingestion]
# MAGIC -->C[Storage]
# MAGIC -->D[Transformation]
# MAGIC -->E[Quality & Governance]
# MAGIC -->F[Lakehouse]
# MAGIC F-->G[Dashboards]
# MAGIC F-->H[Machine Learning]
# MAGIC F-->I[Enterprise RAG]
# MAGIC F-->J[Agentic AI]
# MAGIC ```

# COMMAND ----------

# MAGIC %md
# MAGIC # 🏢 Real Enterprise Example
# MAGIC A retailer receives data from ERP, CRM, mobile apps, payment gateways, warehouses and IoT devices.
# MAGIC
# MAGIC Without Data Engineering:
# MAGIC - Duplicate records
# MAGIC - Missing values
# MAGIC - Conflicting KPIs
# MAGIC - Poor AI responses
# MAGIC
# MAGIC With Data Engineering:
# MAGIC - Trusted datasets
# MAGIC - Consistent KPIs
# MAGIC - Governed access
# MAGIC - Reliable AI applications

# COMMAND ----------

# MAGIC %md
# MAGIC # 🔥 Why It Matters in the AI Era
# MAGIC Modern AI systems require:
# MAGIC - Clean enterprise data
# MAGIC - Metadata
# MAGIC - Documents
# MAGIC - Embeddings
# MAGIC - Vector indexes
# MAGIC - Governance
# MAGIC
# MAGIC **No Data Engineering → No trustworthy AI.**

# COMMAND ----------

# MAGIC %md
# MAGIC # 💻 Lab 1 – Create Your First Spark DataFrame

# COMMAND ----------

products = [
    (1,"Laptop","Electronics",80000),
    (2,"Mouse","Electronics",500),
    (3,"Keyboard","Electronics",2500),
    (4,"Monitor","Electronics",18000),
    (5,"Chair","Furniture",7000)
]

df = spark.createDataFrame(
    products,
    ["product_id","product_name","category","price"]
)

display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Filter Premium Products

# COMMAND ----------

from pyspark.sql.functions import col

premium_df = df.filter(col("price") > 5000)
display(premium_df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Aggregate Sales by Category

# COMMAND ----------

from pyspark.sql.functions import sum

display(
    df.groupBy("category")
      .agg(sum("price").alias("total_price"))
)

# COMMAND ----------

# MAGIC %md
# MAGIC ## SQL Example

# COMMAND ----------

df.createOrReplaceTempView("products")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC   category,
# MAGIC   COUNT(*) AS total_products,
# MAGIC   SUM(price) AS total_price
# MAGIC FROM products
# MAGIC GROUP BY category
# MAGIC ORDER BY total_price DESC;

# COMMAND ----------

# MAGIC %md
# MAGIC ## Save as Delta

# COMMAND ----------

df.write.mode("overwrite").format("delta").save("/tmp/module1/products")

delta_df = spark.read.format("delta").load("/tmp/module1/products")
display(delta_df)

# COMMAND ----------

# MAGIC %md
# MAGIC # 💡 Best Practices
# MAGIC - Treat data as a product.
# MAGIC - Build reusable pipelines.
# MAGIC - Validate data early.
# MAGIC - Automate quality checks.
# MAGIC - Design for scalability.

# COMMAND ----------

# MAGIC %md
# MAGIC # ⚠️ Common Mistakes
# MAGIC - Thinking Data Engineering is only ETL.
# MAGIC - Ignoring data quality.
# MAGIC - Hardcoding configuration.
# MAGIC - Optimizing before measuring.

# COMMAND ----------

# MAGIC %md
# MAGIC # 🎯 Interview Corner
# MAGIC **Typical Questions**
# MAGIC 1. What is Data Engineering?
# MAGIC 2. Why is it important?
# MAGIC 3. How is it different from Data Science?
# MAGIC 4. Why is Data Engineering critical for GenAI?
# MAGIC
# MAGIC **What the interviewer is evaluating**
# MAGIC - Understanding of modern data platforms
# MAGIC - Ability to connect engineering with business outcomes
# MAGIC - Awareness of AI-ready data foundations

# COMMAND ----------

# MAGIC %md
# MAGIC # 📝 Assignment
# MAGIC 1. Add five more products.
# MAGIC 2. Compute average price by category.
# MAGIC 3. Save the result as a Delta table.
# MAGIC 4. Query it using SQL.

# COMMAND ----------

# MAGIC %md
# MAGIC # ✅ Summary
# MAGIC Data Engineering transforms raw enterprise data into trusted information that powers dashboards, machine learning, Enterprise RAG and Agentic AI.
# MAGIC
# MAGIC **Next Topic:** Distributed Computing
