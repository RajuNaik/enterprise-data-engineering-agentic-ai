# Module 1 -- Distributed Data Engineering Foundations

# 2. Distributed Computing

> **Enterprise Data Engineering & Agentic AI (2026 Edition)**

------------------------------------------------------------------------

# Learning Objectives

By the end of this chapter, you will be able to:

-   Explain what distributed computing is.
-   Understand why distributed computing became necessary.
-   Differentiate vertical and horizontal scaling.
-   Understand clusters, nodes, and parallel processing.
-   Explain how Apache Spark leverages distributed computing.
-   Recognize common distributed systems challenges.
-   Relate distributed computing to modern AI and data platforms.

------------------------------------------------------------------------

# Why Distributed Computing?

Imagine processing a **5 KB CSV** on your laptop.

It completes instantly.

Now imagine processing:

-   100 GB
-   10 TB
-   5 PB

Would a single machine still be enough?

Usually not.

The bottlenecks include:

-   CPU
-   Memory
-   Disk
-   Network bandwidth
-   Failure recovery

Instead of buying one extremely powerful computer, modern systems
combine **hundreds or thousands of computers** and process data
simultaneously.

This is **Distributed Computing**.

------------------------------------------------------------------------

# Definition

**Distributed Computing is a computing model where multiple independent
machines collaborate to solve a problem by sharing computation and
storage.**

Instead of:

``` text
One Computer
    │
Process Everything
```

we have:

``` text
Computer A
      │
Computer B
      │
Computer C
      │
Computer D

↓

Process Together
```

------------------------------------------------------------------------

# Everyday Analogy

Imagine sorting **10 million exam papers**.

### Single Teacher

``` text
Teacher

10,000,000 Papers
```

Time: Very long.

### 1,000 Teachers

``` text
Teacher 1

Teacher 2

Teacher 3

...

Teacher 1000
```

Each teacher grades only a small portion.

Everyone works simultaneously.

This is parallel processing.

------------------------------------------------------------------------

# Vertical vs Horizontal Scaling

## Vertical Scaling (Scale Up)

``` text
CPU ↑
RAM ↑
Disk ↑

One Machine
```

Advantages

-   Easy to manage
-   No distributed complexity

Limitations

-   Expensive
-   Hardware limit
-   Single point of failure

------------------------------------------------------------------------

## Horizontal Scaling (Scale Out)

``` text
Machine 1

Machine 2

Machine 3

Machine 4
```

Advantages

-   Near-linear scalability
-   Fault tolerance
-   Cost effective
-   Preferred by cloud platforms

------------------------------------------------------------------------

# Distributed Computing Architecture

``` mermaid
flowchart TD

Client --> Master

Master --> Worker1
Master --> Worker2
Master --> Worker3
Master --> Worker4

Worker1 --> Storage
Worker2 --> Storage
Worker3 --> Storage
Worker4 --> Storage
```

This is the conceptual foundation for Spark clusters.

------------------------------------------------------------------------

# Core Components

  Component             Description
  --------------------- -------------------------------------
  Cluster               Group of computers working together
  Node                  Individual computer in a cluster
  Master                Coordinates work
  Worker                Executes tasks
  Network               Connects all machines
  Distributed Storage   Shared data location

------------------------------------------------------------------------

# Why Apache Spark Uses Distributed Computing

Spark divides work into many small tasks.

Instead of reading one huge file sequentially:

``` text
1 TB File

↓

One Machine

↓

10 Hours
```

Spark partitions the file.

``` text
1 TB

↓

250 GB

250 GB

250 GB

250 GB

↓

4 Workers

↓

Much Faster
```

We'll study partitioning in later chapters.

------------------------------------------------------------------------

# Enterprise Example

An online retailer processes:

-   500 million transactions/day
-   100 TB clickstream/day
-   20 million customer events/hour

A single server cannot process this volume reliably.

A Spark cluster distributes the workload across hundreds of executors.

------------------------------------------------------------------------

# Distributed Computing Challenges

Distributed systems introduce new problems.

## Network Failures

Machines communicate over networks.

Networks fail.

------------------------------------------------------------------------

## Data Skew

One worker may receive significantly more data.

Result:

-   Slow jobs
-   Idle workers

------------------------------------------------------------------------

## Fault Tolerance

Machines crash.

Frameworks like Spark automatically recompute lost work.

------------------------------------------------------------------------

## Synchronization

Multiple workers may update shared state.

Coordination is required.

------------------------------------------------------------------------

## Resource Management

CPU

Memory

Disk

Network

must be efficiently allocated.

------------------------------------------------------------------------

# Distributed Computing in the AI Era

Modern AI platforms process:

-   Enterprise documents
-   Images
-   Audio
-   Videos
-   Embeddings
-   Vector indexes
-   Streaming events

Distributed computing powers:

-   Spark
-   Distributed model training
-   Large-scale feature engineering
-   Enterprise RAG pipelines
-   Agentic AI platforms

------------------------------------------------------------------------

# Hands-on (Concept Demonstration)

Although a Community Edition cluster may have limited resources, this
exercise illustrates partitioning.

## Python Cell

``` python
data = [(i,) for i in range(100)]

df = spark.createDataFrame(data, ["number"])

print("Partitions:", df.rdd.getNumPartitions())
```

## Python Cell

``` python
df = df.repartition(4)

print("Partitions after repartition:", df.rdd.getNumPartitions())
```

## Python Cell

``` python
display(df.groupBy().count())
```

> We will explore partitioning and execution plans in depth in later
> Spark chapters.

------------------------------------------------------------------------

# Best Practices

-   Scale out before scaling up.
-   Partition data intelligently.
-   Minimize unnecessary data movement.
-   Avoid skewed workloads.
-   Monitor cluster utilization.

------------------------------------------------------------------------

# Common Mistakes

-   Assuming more nodes always improve performance.
-   Ignoring partition sizes.
-   Excessive shuffling.
-   Underestimating network latency.
-   Using distributed systems for tiny datasets.

------------------------------------------------------------------------

# Interview Questions

## Beginner

1.  What is distributed computing?
2.  Why do we need distributed computing?
3.  What is a cluster?

## Intermediate

1.  Difference between vertical and horizontal scaling.
2.  What is a worker node?
3.  Why is partitioning important?

## Advanced

1.  Design a system to process 100 TB daily.
2.  How would you mitigate data skew?
3.  Explain how Spark achieves fault tolerance.

------------------------------------------------------------------------

# MANGOS Interview Focus

Senior interviewers often move beyond definitions and ask:

-   When **shouldn't** you use distributed computing?
-   What happens if one node fails?
-   Why doesn't adding more machines always make jobs faster?
-   How do network bandwidth and partitioning influence performance?
-   Explain distributed computing using a real production system you've
    worked on.

------------------------------------------------------------------------

# Key Takeaways

-   Distributed computing enables multiple machines to solve one problem
    together.
-   Horizontal scaling is the foundation of modern cloud-native data
    platforms.
-   Apache Spark is built on distributed computing principles.
-   Understanding clusters, nodes, partitioning, and fault tolerance is
    essential before learning Spark internals.
-   Every modern enterprise AI platform---from feature engineering to
    Agentic AI---depends on distributed computing.
