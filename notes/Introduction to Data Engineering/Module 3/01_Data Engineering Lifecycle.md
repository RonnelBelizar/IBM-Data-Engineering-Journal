# Topic: Module 3 - Data Engineering Lifecycle

# 🏗️ Layers of a Data Platform Architecture

---

## 1. Data Ingestion / Collection
    • What → The entry point; gathers raw data from different sources.  
    • Sources → Databases (SQL/NoSQL), APIs, sensors, logs, social media, files.  
    • How → Batch (scheduled loads) or Streaming (real-time).  
    • Tools → Apache Kafka, Apache NiFi, Talend, Fivetran.  

    ⚠️ Pitfalls if weak →  
        - Missing or delayed data → analytics become outdated.  
        - Poor connectivity → incomplete datasets.  
        - No validation → bad/duplicate data floods the system.  

---

## 2. Data Storage
    • What → Where data is kept after ingestion.  
    • Types →  
        - Databases (OLTP → transactional).  
        - Data Warehouses (structured, analytics-ready).  
        - Data Lakes (raw, unstructured/semi-structured).  
    • Why → To persist data so it can be processed and analyzed later.  
    • Tools → MySQL, PostgreSQL, Snowflake, Redshift, Hadoop HDFS, AWS S3.  

    ⚠️ Pitfalls if weak →  
        - Storage overload → system slows or crashes.  
        - Poor data organization → data swamp (unusable lake).  
        - Lack of backups → risk of permanent data loss.  

---

## 3. Data Processing
    • What → Converts raw data into usable/clean data.  
    • Styles →  
        - Batch Processing → Handle large volumes at once (e.g., nightly jobs).  
        - Stream Processing → Handle real-time continuous flows (e.g., IoT).  
    • Why → Standardize formats, remove errors, enrich with context.  
    • Tools → Apache Spark, Flink, Databricks, Hadoop MapReduce.  

    ⚠️ Pitfalls if weak →  
        - Dirty data remains → bad insights.  
        - Slow jobs → reports delayed.  
        - Wrong transformations → decisions based on false results.  

---

## 4. Analysis and User Interface (UI)
    • What → The layer where data is explored, visualized, and consumed.  
    • Who → Data analysts, scientists, business users.  
    • Why → To generate insights, reports, and decisions.  
    • Tools → Tableau, Power BI, Looker, Jupyter Notebooks, Superset.  

    ⚠️ Pitfalls if weak →  
        - Dashboards inaccurate → trust in data lost.  
        - Poor usability → users avoid platform.  
        - Latency → business can’t act fast enough.  

---

## 5. Data Pipeline (The Glue)
    • What → The automated workflow connecting all layers above.  
    • Flow →  
        - Ingest → Store → Process → Analyze → Deliver.  
    • Why → Ensures data moves reliably and consistently from source to insights.  
    • Tools → Apache Airflow, Luigi, Prefect, AWS Data Pipeline.  

    ⚠️ Pitfalls if weak →  
        - Pipeline breaks → data doesn’t flow = no insights.  
        - Lack of monitoring → silent failures.  
        - Over-complex design → hard to maintain, costly.  

---

## 🔗 How They Relate
    • Ingestion → Brings data into the platform.  
    • Storage → Holds it in a structured/unstructured way.  
    • Processing → Transforms raw → usable form.  
    • Analysis/UI → Lets humans and apps extract insights.  
    • Pipeline → Automates + orchestrates everything across layers.  

    ⚡ Think of it like:  
        - Ingestion = Pipes bringing water.  
        - Storage = Water tanks.  
        - Processing = Filters + treatment.  
        - Analysis/UI = Faucet where you drink or use the water.  
        - Pipeline = Plumbing connecting it all together.  

    ❗ If one layer fails → the whole system weakens.  
        - Bad ingestion → garbage data enters.  
        - Weak storage → data gets lost or messy.  
        - Poor processing → insights wrong.  
        - Bad UI → users don’t trust results.  
        - Broken pipeline → no flow = dead system.  

---

# 🗄️ Factors for Designing and Selecting Data Stores

---

## 1. Primary Considerations
    • What kind of data do you have? (structured, semi-structured, unstructured).  
    • How will the data be queried? (SQL, API, search).  
    • Do you need real-time or batch access?  
    • What are the latency + performance needs?  
    • Budget + scaling needs (cloud vs on-prem).  

---

## 2. Types of Databases
    • Relational Databases (RDBMS) → Structured, tables + SQL.  
        - Examples: MySQL, PostgreSQL, Oracle, SQL Server.  
    • NoSQL Databases → Flexible, handles scale + diverse data.  
        - Examples: MongoDB, Cassandra, Redis, Neo4j.  

---

## 3. Four Types of NoSQL
    • Document Stores → JSON-like, semi-structured.  
        - Examples: MongoDB, CouchDB.  
    • Key-Value Stores → Fast, simple retrieval by key.  
        - Examples: Redis, DynamoDB.  
    • Columnar Stores → Efficient for wide, large datasets.  
        - Examples: Cassandra, HBase.  
    • Graph Databases → Relationships between entities.  
        - Examples: Neo4j, Amazon Neptune.  

---

## 4. Volume / Scale of Data
    • Small datasets → RDBMS is often enough.  
    • Very large datasets → NoSQL, Data Lakes, Big Data systems.  
    • Real-time high-volume → Streaming DBs + NoSQL.  
    • Archival/historical → Warehouses or cold storage.  

---

## 5. Intended Use of Collected Data
    • Transactional (OLTP) → Frequent updates, small fast queries.  
        - Example: Banking, e-commerce carts.  
    • Analytical (OLAP) → Complex queries, large aggregations.  
        - Example: Yearly sales reports, hospital analytics.  
    • AI/ML Workloads → Flexible, fast access to large varied datasets.  
        - Example: Patient risk prediction using EMR + imaging data.  

---

## 6. Storage Considerations
    • Performance → Latency, read/write speeds.  
    • Reliability → Backups, fault tolerance, replication.  
    • Security → Access control, encryption, compliance (HIPAA, GDPR).  
    • Cost → Cloud pricing (storage + compute), licenses.  
    • Scalability → Horizontal (add machines) vs Vertical (bigger machine).  
    • Data Growth → Can it handle tomorrow’s scale?  

---

## 🔑 Summary
    • The “right” data store depends on → data type, size, usage, speed, and cost.  
    • RDBMS → best for structured + consistent transactions.  
    • NoSQL → best for scale, flexibility, and modern apps.  
    • Volume + growth + workload → determine long-term fit.  

---

# 🔒 Security in Data Engineering

---

## 1. The CIA Triad
    • Confidentiality → Keep data private (only authorized access).  
    • Integrity → Ensure data is accurate + not tampered with.  
    • Availability → Systems/data must be accessible when needed.  

---

## 2. Physical Infrastructure Security
    • Protect data centers and hardware.  
    • Examples: locked server rooms, biometric access, CCTV, disaster recovery plans.  
    • Cloud: relies on provider’s physical security (AWS, GCP, Azure).  

---

## 3. Network Security
    • Protects communication channels and data transfer.  
    • Firewalls → Block unauthorized traffic.  
    • VPNs → Secure remote access.  
    • IDS/IPS → Intrusion detection/prevention systems.  
    • TLS/SSL → Encrypts data over the internet.  

---

## 4. Application Security
    • Securing the apps that interact with data.  
    • Authentication → Verifying user identity (e.g., passwords, MFA, SSO).  
    • Authorization → Defining what actions/data users can access.  
    • Input validation → Prevent SQL injection, XSS attacks.  
    • Regular patches → Keep software updated.  

---

## 5. Data Security
    • Protects the actual data itself (regardless of where it lives).  

    🔹 Data at Rest  
        - Stored data (DBs, disks, backups).  
        - Protection: encryption (AES-256), access controls, secure storage.  

    🔹 Data in Transit  
        - Moving data (APIs, pipelines, streaming).  
        - Protection: encryption (TLS/SSL, HTTPS, VPN), secure protocols (SFTP).  

    🔹 Data in Use (bonus)  
        - Data being actively processed in memory.  
        - Protection: secure enclaves, masking, tokenization.  

---

## 🔑 Summary
    • Security must be layered (physical → network → apps → data).  
    • CIA triad is the foundation: keep data safe, accurate, and available.  
    • Encryption, access control, and monitoring are must-haves.  
    • Cloud providers cover infra, but you must secure apps + data use.  

---









