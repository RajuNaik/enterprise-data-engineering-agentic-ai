# Databricks notebook source
# COMMAND ----------
# MAGIC %md
# MAGIC <div style="background:#0F172A;color:white;padding:18px;border-radius:10px">
# MAGIC <h1>Enterprise Data Engineering & Agentic AI Mastery (2026)</h1>
# MAGIC <h2>Module 1 • Notebook 03</h2>
# MAGIC <h2>OLTP vs OLAP</h2>
# MAGIC <b>Difficulty:</b> Beginner → Intermediate &nbsp; | &nbsp; <b>Duration:</b> 90 Minutes
# MAGIC </div>

# COMMAND ----------
# MAGIC %md
# MAGIC ## 🎯 Learning Objectives
# MAGIC - Understand why OLTP and OLAP were invented
# MAGIC - Compare transactional and analytical databases
# MAGIC - Learn row-store vs column-store
# MAGIC - Understand normalization vs denormalization
# MAGIC - Connect OLTP → CDC → Lakehouse → AI

# COMMAND ----------
# MAGIC %md
# MAGIC ## 🌍 Enterprise Story
# MAGIC A customer purchases a laptop from an e-commerce website.
# MAGIC The checkout transaction must finish in milliseconds (OLTP), while management wants dashboards showing sales by region, product and month (OLAP). Running analytical queries on the checkout database would slow customer transactions, so enterprises separate operational and analytical workloads.

# COMMAND ----------
# MAGIC %md
# MAGIC ## 🏗 End-to-End Enterprise Flow
# MAGIC ```mermaid
# MAGIC flowchart LR
# MAGIC A[Customer/App]-->B[(OLTP Database)]
# MAGIC B-->C[CDC]
# MAGIC C-->D[Bronze]
# MAGIC D-->E[Silver]
# MAGIC E-->F[Gold]
# MAGIC F-->G[Power BI]
# MAGIC F-->H[Machine Learning]
# MAGIC F-->I[Enterprise RAG]
# MAGIC I-->J[Agentic AI]
# MAGIC ```

# COMMAND ----------
# MAGIC %md
# MAGIC ## 📘 What is OLTP?
# MAGIC **Online Transaction Processing** focuses on day-to-day business operations.
# MAGIC Typical operations are INSERT, UPDATE and DELETE with strict ACID guarantees.

# COMMAND ----------
# MAGIC %md
# MAGIC ## 📘 What is OLAP?
# MAGIC **Online Analytical Processing** is designed for historical analysis, reporting,
# MAGIC business intelligence and AI workloads over large datasets.

# COMMAND ----------
# MAGIC %md
# MAGIC ## 📊 Comparison
# MAGIC | Feature | OLTP | OLAP |
# MAGIC |---|---|---|
# MAGIC | Primary Goal | Run Business | Analyze Business |
# MAGIC | Storage | Row | Column |
# MAGIC | Schema | Normalized | Star/Snowflake |
# MAGIC | Queries | Short | Complex |
# MAGIC | Updates | Frequent | Rare |
# MAGIC | Users | Applications | Analysts, BI, AI |

# COMMAND ----------
# MAGIC %md
# MAGIC ## 💡 Did You Know?
# MAGIC Modern Lakehouse platforms eliminate multiple copies of data by providing a unified platform for BI, ML and AI.

# COMMAND ----------
# MAGIC %md
# MAGIC ## ⚠️ Interview Trap
# MAGIC Many candidates say **OLAP replaces OLTP**.
# MAGIC It doesn't.
# MAGIC They solve different business problems and complement each other.

# COMMAND ----------
orders=[(1,101,"Laptop",85000),(2,102,"Mouse",1200),(3,101,"Keyboard",3200),(4,103,"Monitor",18000)]
df=spark.createDataFrame(orders,["order_id","customer_id","product","amount"])
display(df)

# COMMAND ----------
from pyspark.sql.functions import sum,count
display(df.groupBy("customer_id").agg(count("*").alias("orders"),sum("amount").alias("revenue")))

# COMMAND ----------
df.createOrReplaceTempView("orders")

# COMMAND ----------
# MAGIC %sql
# MAGIC SELECT customer_id,
# MAGIC COUNT(*) orders,
# MAGIC SUM(amount) revenue
# MAGIC FROM orders
# MAGIC GROUP BY customer_id
# MAGIC ORDER BY revenue DESC;

# COMMAND ----------
# MAGIC %md
# MAGIC ## 🤖 AI Perspective
# MAGIC Enterprise LLMs and Agentic AI should not query OLTP systems directly.
# MAGIC They rely on curated analytical data in a Lakehouse built from CDC pipelines.

# COMMAND ----------
# MAGIC %md
# MAGIC ## 🏢 Enterprise Examples
# MAGIC - Banking: Transactions → Fraud Analytics
# MAGIC - Retail: Orders → Customer Insights
# MAGIC - Airline: Bookings → Demand Forecasting
# MAGIC - Healthcare: EMR → Population Analytics

# COMMAND ----------
# MAGIC %md
# MAGIC ## 📝 Assignment
# MAGIC 1. Create 1 million synthetic orders using spark.range().
# MAGIC 2. Aggregate revenue by customer.
# MAGIC 3. Explain why this workload is OLAP.
# MAGIC 4. Save results as Delta.

# COMMAND ----------
# MAGIC %md
# MAGIC ## 📌 Quick Revision
# MAGIC - OLTP = Operational
# MAGIC - OLAP = Analytical
# MAGIC - CDC bridges both
# MAGIC - Lakehouse powers BI + ML + AI
