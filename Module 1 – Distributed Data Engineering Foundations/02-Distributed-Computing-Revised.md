# Module 1 -- Distributed Data Engineering Foundations

# 2. Distributed Computing

> **Enterprise Data Engineering & Agentic AI (2026 Edition)**

------------------------------------------------------------------------

# Learning Objectives

After completing this chapter, you will be able to:

-   Explain distributed computing from first principles.
-   Understand why modern enterprises use clusters instead of single
    machines.
-   Differentiate vertical and horizontal scaling.
-   Understand clusters, nodes, master and worker nodes.
-   Explain how Apache Spark uses distributed computing.
-   Identify common distributed systems challenges.
-   Perform a simple partitioning exercise in Databricks.

------------------------------------------------------------------------

# Why Distributed Computing?

In the early days, applications ran on a single server. As data volumes
grew from megabytes to terabytes and petabytes, one machine became a
bottleneck.

Typical limitations include:

-   Limited CPU cores
-   Limited RAM
-   Limited storage
-   Hardware failures
-   Long processing times

Instead of purchasing one extremely large server, organizations connect
many computers together and divide the workload among them.

This approach is called **Distributed Computing**.

------------------------------------------------------------------------

# Definition

**Distributed Computing is a computing model in which multiple
independent computers collaborate over a network to solve a problem by
sharing computation, memory and storage.**

------------------------------------------------------------------------

# Real-world Analogy

Imagine evaluating **1 million exam papers**.

### Single Teacher

``` text
1 Teacher
    │
1,000,000 Papers
```

Completion time would be very long.

### 1,000 Teachers

``` text
Teacher 1   → 1,000 papers
Teacher 2   → 1,000 papers
...
Teacher 1000→ 1,000 papers
```

Everyone works in parallel and finishes much faster.

This is exactly how distributed computing works.

------------------------------------------------------------------------

# Vertical vs Horizontal Scaling

  Vertical Scaling (Scale Up)   Horizontal Scaling (Scale Out)
  ----------------------------- --------------------------------
  Add CPU/RAM to one server     Add more servers
  Simple architecture           Distributed architecture
  Hardware limit exists         Scales almost indefinitely
  Single point of failure       Higher fault tolerance
  Expensive                     Cost-effective in the cloud

------------------------------------------------------------------------

# Core Components of a Distributed Computing System

A distributed computing system is made up of several components that
work together to process large volumes of data efficiently.

Think of it as a company with a manager, employees, offices, and a
shared filing system.

## 1. Cluster

A **cluster** is a collection of multiple computers (called nodes) that
work together as if they were one powerful computer.

``` text
Cluster
│
├── Node 1
├── Node 2
├── Node 3
└── Node 4
```

If each machine has 16 CPU cores and 64 GB RAM, the cluster provides a
combined pool of resources.

------------------------------------------------------------------------

## 2. Node

A **node** is an individual computer in a cluster.

Each node has:

-   CPU
-   Memory
-   Disk
-   Network
-   Operating System

Nodes communicate with each other over the network.

------------------------------------------------------------------------

## 3. Master Node

The **Master Node** coordinates the cluster.

Responsibilities:

-   Accept jobs
-   Divide jobs into tasks
-   Schedule tasks
-   Monitor execution
-   Detect failures
-   Collect results

Think of it as the project manager of a construction site.

------------------------------------------------------------------------

## 4. Worker Nodes

Worker nodes perform the actual computation.

Example:

``` text
Worker 1 → 250 Million Records

Worker 2 → 250 Million Records

Worker 3 → 250 Million Records

Worker 4 → 250 Million Records
```

All workers execute simultaneously.

------------------------------------------------------------------------

## 5. Network

The network connects all nodes.

It enables:

-   Task assignment
-   Data transfer
-   Heartbeats
-   Failure detection

Poor network performance directly impacts distributed jobs.

------------------------------------------------------------------------

## 6. Distributed Storage

Large datasets are stored across multiple servers.

Examples:

-   Azure Data Lake Storage
-   Amazon S3
-   Google Cloud Storage
-   HDFS

``` text
1 TB File

↓

Block 1 → Server A
Block 2 → Server B
Block 3 → Server C
Block 4 → Server D
```

Multiple workers read different blocks simultaneously.

------------------------------------------------------------------------

# How Everything Works Together

``` mermaid
flowchart TD
U[User]
M[Master Node]
W1[Worker 1]
W2[Worker 2]
W3[Worker 3]
S[Distributed Storage]

U --> M
M --> W1
M --> W2
M --> W3
W1 --> S
W2 --> S
W3 --> S
```

------------------------------------------------------------------------

# Why Spark Uses Distributed Computing

Spark partitions large datasets into smaller chunks.

Instead of one computer processing a 1 TB file, many executors process
partitions in parallel, reducing execution time dramatically.

------------------------------------------------------------------------

# Enterprise Example

A ride-sharing company ingests:

-   200 million trips/day
-   GPS updates every few seconds
-   Driver events
-   Customer events
-   Payments

A single server cannot process this volume within business SLAs. A Spark
cluster distributes the work across many worker nodes.

------------------------------------------------------------------------

# Common Challenges

-   Data Skew
-   Network Latency
-   Node Failures
-   Resource Contention
-   Excessive Data Shuffle

Each will be covered in later chapters.

------------------------------------------------------------------------

# Hands-on (Databricks)

## Python Cell 1

``` python
data = [(i,) for i in range(100)]

df = spark.createDataFrame(data, ["number"])

print("Initial Partitions:", df.rdd.getNumPartitions())
```

## Python Cell 2

``` python
df = df.repartition(4)

print("Partitions After Repartition:", df.rdd.getNumPartitions())
```

## Python Cell 3

``` python
display(df)
```

------------------------------------------------------------------------

# Interview Corner

### Beginner

-   What is distributed computing?
-   What is a cluster?
-   What is a node?

### Intermediate

-   Difference between scale-up and scale-out.
-   Why is distributed computing fault tolerant?

### Advanced

-   Design a platform that processes 100 TB/day.
-   How would you handle data skew?

------------------------------------------------------------------------

# MANGOS Interview Insight

Senior interviewers often ask **why** distributed computing is needed
instead of simply buying a bigger server. A strong answer should discuss
scalability, fault tolerance, elasticity, cost, and parallel
processing---not just performance.

------------------------------------------------------------------------

# Key Takeaways

-   Distributed computing solves problems that exceed the capacity of a
    single machine.
-   Clusters consist of master and worker nodes connected by a network.
-   Distributed storage enables parallel data access.
-   Apache Spark is built on distributed computing principles.
-   Understanding these concepts is essential before studying Spark
    Architecture.
