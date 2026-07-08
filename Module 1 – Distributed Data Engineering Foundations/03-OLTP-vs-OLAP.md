# Module 1 -- Distributed Data Engineering Foundations

# 3. OLTP vs OLAP

> **Enterprise Data Engineering & Agentic AI (2026 Edition)**

------------------------------------------------------------------------

# Learning Objectives

By the end of this chapter, you will be able to:

-   Explain the purpose of OLTP and OLAP systems.
-   Identify the key differences between transactional and analytical
    workloads.
-   Understand where OLTP and OLAP fit in a modern data platform.
-   Recognize why Spark and Databricks are designed for OLAP workloads.
-   Answer interview questions ranging from beginner to architect level.

------------------------------------------------------------------------

# Why Should You Learn This?

One of the most common interview questions is:

> **"Explain the difference between OLTP and OLAP."**

Most candidates answer with only:

-   OLTP = Transactions
-   OLAP = Analytics

That answer is incomplete.

A senior engineer is expected to explain **why these systems evolved,
how they differ internally, and where each fits in a modern enterprise
architecture.**

------------------------------------------------------------------------

# A Story Before We Begin

Imagine you are using an online shopping application.

When you click **Buy Now**, the application must:

-   Check inventory
-   Verify payment
-   Create an order
-   Update stock
-   Generate an invoice

This entire process must finish in milliseconds.

Now imagine the CEO asks:

> "Show me the sales trend for the last five years by country, product
> category and customer segment."

This query scans billions of rows and performs aggregations.

Clearly, these two workloads are very different.

This is why enterprises use **two different classes of databases**.

------------------------------------------------------------------------

# What is OLTP?

**OLTP (Online Transaction Processing)** systems are optimized for
handling a large number of small, fast, concurrent transactions.

Typical operations:

-   INSERT
-   UPDATE
-   DELETE
-   Simple SELECT

Examples:

-   ATM withdrawal
-   Airline ticket booking
-   Food delivery order
-   UPI payment
-   Hospital registration
-   E-commerce checkout

------------------------------------------------------------------------

# Characteristics of OLTP

  Characteristic   Description
  ---------------- ---------------------------
  Workload         Transactions
  Queries          Short
  Response Time    Milliseconds
  Users            Thousands to millions
  Data Model       Highly normalized
  Data Size        GB to TB
  Focus            Fast writes & consistency

------------------------------------------------------------------------

# What is OLAP?

**OLAP (Online Analytical Processing)** systems are designed to analyze
large volumes of historical data for business intelligence, reporting,
machine learning and AI.

Typical operations:

-   GROUP BY
-   Aggregations
-   Window Functions
-   Trend Analysis
-   Forecasting

Examples:

-   Monthly sales report
-   Inventory optimization
-   Customer segmentation
-   Financial reporting
-   AI feature engineering

------------------------------------------------------------------------

# Characteristics of OLAP

  Characteristic   Description
  ---------------- ---------------------------
  Workload         Analytics
  Queries          Complex
  Response Time    Seconds to minutes
  Data Model       Dimensional / Lakehouse
  Data Size        TB to PB
  Focus            Fast reads & aggregations

------------------------------------------------------------------------

# Visual Comparison

``` mermaid
flowchart LR

A[Customer Places Order]
B[(OLTP Database)]
C[CDC / ETL / Streaming]
D[(Data Warehouse / Lakehouse)]
E[Dashboard]
F[Machine Learning]
G[Agentic AI]

A --> B
B --> C
C --> D
D --> E
D --> F
D --> G
```

------------------------------------------------------------------------

# OLTP vs OLAP Comparison

  ------------------------------------------------------------------------
  Feature                      OLTP                  OLAP
  ---------------------------- --------------------- ---------------------
  Purpose                      Run business          Analyze business
                               operations            

  Data                         Current               Historical + Current

  Reads/Writes                 Many writes           Mostly reads

  Query Complexity             Simple                Complex

  Concurrency                  Very High             Moderate

  Normalization                Highly normalized     Denormalized / Star
                                                     Schema

  Users                        End users             Analysts, Engineers,
                                                     AI Systems

  Example Technologies         MySQL, PostgreSQL,    Spark, Databricks,
                               Oracle                Snowflake, BigQuery
  ------------------------------------------------------------------------

------------------------------------------------------------------------

# Enterprise Architecture

``` text
Customers
     │
     ▼
 OLTP Systems
 (ERP / CRM / Banking)
     │
     ▼
Ingestion (CDC, ETL, Streaming)
     │
     ▼
Data Lakehouse
     │
 ┌───┼───────────────┐
 ▼   ▼               ▼
BI  ML          Agentic AI
```

------------------------------------------------------------------------

# Why Spark is an OLAP Engine

Apache Spark is **not** designed to replace OLTP databases.

Spark excels at:

-   Reading billions of records
-   Parallel processing
-   Aggregations
-   Machine Learning
-   Batch & Streaming Analytics

Spark is inefficient for:

-   Updating one customer record at a time
-   Processing millions of tiny transactions per second

Those workloads belong to OLTP databases.

------------------------------------------------------------------------

# Practical Example

## OLTP SQL

``` sql
UPDATE accounts
SET balance = balance - 500
WHERE account_id = 1001;
```

This updates a single record and must complete immediately.

------------------------------------------------------------------------

## OLAP SQL

``` sql
SELECT
    country,
    SUM(sales) AS total_sales
FROM sales
GROUP BY country
ORDER BY total_sales DESC;
```

This scans millions of records to produce business insights.

------------------------------------------------------------------------

# Databricks Practice

## Python Cell

``` python
sales = [
    ("India","Laptop",80000),
    ("India","Mouse",500),
    ("USA","Laptop",1200),
    ("USA","Monitor",350)
]

df = spark.createDataFrame(
    sales,
    ["country","product","sales"]
)

display(df)
```

## SQL Cell

``` sql
SELECT
    country,
    SUM(sales) AS total_sales
FROM sales
GROUP BY country
ORDER BY total_sales DESC;
```

> Before executing the SQL query, register the DataFrame:

``` python
df.createOrReplaceTempView("sales")
```

------------------------------------------------------------------------

# Common Misconceptions

❌ OLTP databases are "better" than OLAP databases.

✔ They solve different problems.

------------------------------------------------------------------------

❌ Spark can replace Oracle.

✔ Spark complements transactional databases; it is not a replacement.

------------------------------------------------------------------------

❌ OLAP stores only historical data.

✔ Modern Lakehouses support both historical and near real-time
analytical data.

------------------------------------------------------------------------

# Enterprise Case Study

A retailer processes millions of purchases daily.

**OLTP**

-   Customer checkout
-   Inventory update
-   Payment processing

**OLAP**

Every night (or continuously via streaming), transaction data is loaded
into a Lakehouse where analysts answer:

-   Which products are selling fastest?
-   Which regions are underperforming?
-   Which customers should receive promotions?
-   Which products should feed recommendation engines?

The same curated data later powers enterprise RAG and Agentic AI
assistants.

------------------------------------------------------------------------

# MANGOS Interview Focus

Senior interviewers often ask:

-   Why can't Spark replace PostgreSQL?
-   Why are OLTP databases normalized?
-   Why are OLAP systems often denormalized?
-   Why is columnar storage preferred for analytics?
-   How do CDC pipelines connect OLTP and OLAP?

------------------------------------------------------------------------

# Best Practices

-   Never run heavy analytical queries on production OLTP databases.
-   Separate operational and analytical workloads.
-   Use CDC for near real-time synchronization.
-   Optimize OLAP using partitioning, file formats and distributed
    processing.

------------------------------------------------------------------------

# Key Takeaways

-   OLTP powers day-to-day business transactions.
-   OLAP powers analytics, reporting, machine learning and AI.
-   Spark and Databricks belong to the OLAP ecosystem.
-   Modern enterprises connect OLTP and OLAP through streaming and CDC
    pipelines.
-   Understanding this distinction is fundamental before learning Data
    Lakes, Lakehouses and Apache Spark.

------------------------------------------------------------------------

# Next Chapter

**Data Warehouse vs Data Lake vs Lakehouse**
