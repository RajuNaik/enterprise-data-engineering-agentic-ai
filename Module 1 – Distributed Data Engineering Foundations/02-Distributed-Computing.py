# Databricks notebook source
# MAGIC %md
# MAGIC <div style="background:#0B3B60;color:white;padding:18px;border-radius:10px">
# MAGIC <h1>Enterprise Data Engineering & Agentic AI (2026 Edition)</h1>
# MAGIC <h2>Module 1 – Distributed Data Engineering Foundations</h2>
# MAGIC <h2>Notebook 02 – Distributed Computing</h2>
# MAGIC <b>Level:</b> Beginner → Intermediate | <b>Duration:</b> 60 Minutes
# MAGIC </div>

# COMMAND ----------
# MAGIC %md
# MAGIC # 🎯 Learning Objectives
# MAGIC - Understand distributed computing fundamentals
# MAGIC - Learn clusters, nodes, drivers and executors
# MAGIC - Compare vertical vs horizontal scaling
# MAGIC - Practice partitioning in Spark

# COMMAND ----------
# MAGIC %md
# MAGIC # 🌍 Enterprise Story
# MAGIC Imagine an airline generates billions of telemetry events every day.
# MAGIC A single server cannot process this workload within SLA.
# MAGIC Distributed Computing allows many computers to work together.

# COMMAND ----------
# MAGIC %md
# MAGIC # 📊 Scale Up vs Scale Out
# MAGIC | Vertical Scaling | Horizontal Scaling |
# MAGIC |---|---|
# MAGIC | Bigger Server | More Servers |
# MAGIC | Hardware Limit | Near Unlimited |
# MAGIC | Single Failure | Fault Tolerant |
# MAGIC | Expensive | Cloud Friendly |

# COMMAND ----------
# MAGIC %md
# MAGIC # 🏗️ Cluster Architecture
# MAGIC ```mermaid
# MAGIC flowchart TD
# MAGIC U[Notebook]-->D[Driver]
# MAGIC D-->E1[Executor 1]
# MAGIC D-->E2[Executor 2]
# MAGIC D-->E3[Executor 3]
# MAGIC E1-->S[(Storage)]
# MAGIC E2-->S
# MAGIC E3-->S
# MAGIC ```

# COMMAND ----------
# MAGIC %md
# MAGIC # ⚙️ Under the Hood
# MAGIC 1. Driver receives Spark code.
# MAGIC 2. Data is partitioned.
# MAGIC 3. Tasks are scheduled.
# MAGIC 4. Executors process partitions in parallel.
# MAGIC 5. Results are returned.

# COMMAND ----------
# MAGIC %md
# MAGIC # 💻 Lab - Partitioning

# COMMAND ----------
data=[(i,f"Record-{i}") for i in range(1000)]
df=spark.createDataFrame(data,["id","name"])
print(df.rdd.getNumPartitions())
display(df.limit(10))

# COMMAND ----------
df=df.repartition(4)
print(df.rdd.getNumPartitions())

# COMMAND ----------
from pyspark.sql.functions import spark_partition_id,count
display(df.groupBy(spark_partition_id().alias("partition")).agg(count("*").alias("rows")))

# COMMAND ----------
df.explain(True)

# COMMAND ----------
df.createOrReplaceTempView("records")

# COMMAND ----------
# MAGIC %sql
# MAGIC SELECT COUNT(*) total_records, MIN(id) min_id, MAX(id) max_id FROM records;

# COMMAND ----------
# MAGIC %md
# MAGIC # 🤖 AI Perspective
# MAGIC Distributed computing powers Feature Engineering, Enterprise RAG, Vector Search and Agentic AI.

# COMMAND ----------
# MAGIC %md
# MAGIC # 🎯 Interview Questions
# MAGIC - Why distributed computing?
# MAGIC - Why not buy a bigger server?
# MAGIC - What is partitioning?
# MAGIC - Cluster vs Node?
# MAGIC - Driver vs Executor?

# COMMAND ----------
# MAGIC %md
# MAGIC # 📝 Assignment
# MAGIC - Create 1 million records using spark.range().
# MAGIC - Compare repartition(4) and repartition(8).
# MAGIC - Observe execution plans.
# MAGIC - Save as Delta.

# COMMAND ----------
# MAGIC %md
# MAGIC # ✅ Summary
# MAGIC Distributed Computing enables Spark to scale across many machines and forms the foundation of modern Data Engineering.
