# Topic: Module 2 - Data Engineering Lifecycle

# 🗄️ SQL – Querying & Analyzing Data

---

## 📌 What is SQL?
    • Structured Query Language (SQL) → Standard language for relational databases (RDBMS).
    • Used to store, query, update, and analyze structured data (rows + columns).
    • Core skill in data engineering, analytics, and BI.

---

## ✅ Why SQL is Used
    • Universal → Works with most RDBMS (MySQL, PostgreSQL, Oracle, SQL Server, IBM Db2).
    • Powerful for querying → Filtering, aggregations, joins.
    • Ensures data consistency and integrity.
    • Works across OLTP (transactions) and OLAP (analytics).
    • Standardized → SQL knowledge transfers between systems.

---

## ❌ Limitations of SQL
    • Fixed schema → Not flexible for unstructured/semi-structured data.
    • Scaling → Large datasets need heavy infrastructure (expensive).
    • Complex queries → May get slow with massive data.
    • Less adaptable compared to NoSQL for high-volume + diverse data.

---

## 🔹 Key SQL Operations
    • SELECT … FROM … → Retrieve data.
    • WHERE → Filter rows.
    • ORDER BY → Sort results.
    • GROUP BY + HAVING → Aggregations.
    • JOIN → Combine multiple tables.
    • UNION / INTERSECT / EXCEPT → Set operations.
    • INSERT, UPDATE, DELETE → Data manipulation.

---

## 🛠️ Examples of SQL Systems
    • MySQL → Open-source, widely used.
    • PostgreSQL → Open-source, advanced features.
    • Oracle Database → Enterprise, commercial.
    • Microsoft SQL Server → Enterprise + BI support.
    • IBM Db2 → IBM’s relational database.

---

## 💻 Sample SQL Queries

    ### 1. Select Data
        SELECT name, age
        FROM patients;

    ### 2. Filter Data
        SELECT name, age
        FROM patients
        WHERE age > 60;

    ### 3. Sort Data
        SELECT name, age
        FROM patients
        ORDER BY age DESC;

    ### 4. Aggregate Data
        SELECT COUNT(*) AS total_patients, AVG(age) AS avg_age
        FROM patients;

    ### 5. Grouping
        SELECT site_id, COUNT(*) AS test_count
        FROM tests
        GROUP BY site_id;

    ### 6. Join Tables
        SELECT p.name, t.result
        FROM patients p
        INNER JOIN tests t
        ON p.patient_id = t.patient_id;

    ### 7. Insert New Data
        INSERT INTO patients (patient_id, name, age)
        VALUES (101, 'Alice', 45);

    ### 8. Update Data
        UPDATE patients
        SET age = 46
        WHERE patient_id = 101;

    ### 9. Delete Data
        DELETE FROM patients
        WHERE patient_id = 101;

---

## 🔑 Summary
    • SQL is the backbone of querying and analyzing structured data.
    • Best suited for structured + relational systems.
    • Still critical in modern big data — many tools (Hive, SparkSQL) use SQL-like syntax.

---

# ⚡ Performance Tuning & Troubleshooting

---

## 📌 Why It Matters
    • In data engineering, system performance = reliability + user trust.  
    • Bottlenecks (slow queries, outages, overloaded resources) directly affect analytics and operations.  
    • Tuning ensures data systems stay responsive, cost-efficient, and scalable.  

---

## 📊 Performance Metrics
    • Latency → Time taken for requests/queries to respond.  
    • Failures → System crashes, errors, or failed queries.  
    • Resource Utilization → CPU, memory, disk, and network usage.  
    • Traffic → Number of requests/users hitting the system.  
    • Throughput → How much data/queries are processed per unit time.  
    • Availability → % of time system is operational (e.g., 99.9% uptime).  

---

## 🛠️ Troubleshooting Steps
    • Collect information → Identify the "what, where, when."  
    • Verify software version → Some issues are version-specific.  
    • Analyze logs & metrics → Error logs, query execution plans, system metrics.  
    • Reproduce in test environment → Validate if the problem can be isolated.  
    • Apply quick fixes first → Kill runaway queries, clear cache, restart services.  
    • Document issues & solutions → Helps future troubleshooting.  

---

## 📊 Performance Metrics for Databases
    • System Outages → Complete downtime.  
    • Capacity Utilization → Is the DB close to storage/compute limits?  
    • Application Slowdown → Noticeable lag for users.  
    • Query Performance → Long execution times, missing indexes.  
    • Conflicting Queries → Multiple heavy queries competing for the same resources.  
    • Batch Activities → Nightly/weekly jobs consuming resources and affecting real-time queries.  
    • Locking & Deadlocks → Queries blocking each other and stalling execution.  

---

## ✅ Best Practices for Performance
    • Capacity Planning → Forecast storage & compute needs before issues arise.  
    • Database Indexing → Create indexes to speed up searches (but don’t over-index).  
    • Database Partitioning → Split large tables into smaller chunks for faster access.  
    • Database Normalization → Organize schema to avoid redundancy and improve efficiency.  
    • Monitoring Systems → Continuous tracking of health & performance.  

        🔧 Tools  
            - Application Performance Monitoring (APM) → Dynatrace, New Relic, AppDynamics.  
            - Query Performance Monitoring → SQL execution plans, EXPLAIN, pg_stat_statements.  
            - Job Runtime Monitoring → Track ETL/ELT tasks (Airflow, Luigi, Prefect).  
            - Data Throughput Monitoring → Volume of data processed per pipeline.  

    • Maintenance Schedules  
        - Time-based → Regular maintenance windows (weekly, monthly).  
        - Condition-based → Triggered when metrics show anomalies (e.g., high latency).  

---

## 🎯 Bonus Info: Common SQL Performance Issues & Fixes
    • Missing Indexes → Queries scanning entire tables instead of using indexes.  
        👉 Fix: Add appropriate indexes on WHERE, JOIN, ORDER BY columns.  

    • Too Many Indexes → Every insert/update slows down because indexes must update too.  
        👉 Fix: Only index what you need.  

    • Poor Query Design → SELECT * or unnecessary joins slow queries.  
        👉 Fix: Select only required columns; review joins.  

    • Large Transactions → Long locks, high rollback costs.  
        👉 Fix: Break big transactions into smaller chunks.  

    • Inefficient Joins → Joining massive tables without keys/indexes.  
        👉 Fix: Use indexed keys, consider denormalization if joins are too frequent.  

    • Lack of Caching → Repeated queries hitting DB instead of cache.  
        👉 Fix: Use caching layers (Redis, Memcached).  

    • Hardware Limits → Disk I/O, memory, or CPU bottlenecks.  
        👉 Fix: Scale vertically (bigger server) or horizontally (sharding/replication).  

---

## 🔑 Summary
    • Performance tuning = balancing speed, reliability, and resource efficiency.  
    • Monitoring + proactive maintenance prevents major outages.  
    • Good design (indexes, partitions, normalization) helps avoid bottlenecks.  
    • Troubleshooting requires structured steps: collect data → analyze logs → isolate → fix.  
    • SQL performance often comes down to indexing, query design, and capacity management.  

---

# 🛡️ Data Governance & Compliance

---

## 📌 Why It Matters
    • Ensures data is handled securely, ethically, and legally.  
    • Protects sensitive information from misuse or breaches.  
    • Builds trust with users, customers, and regulators.  
    • Non-compliance can lead to huge fines, reputational damage, or legal action.  

---

## 🏛️ Governance (Frameworks & Regulations)

    • 🌍 GDPR (General Data Protection Regulation – EU)  
      Protects personal data & privacy of EU citizens.  
      Requires consent, right to be forgotten, and breach notification.  

    • 🇺🇸 CCPA (California Consumer Privacy Act – USA)  
      Gives consumers rights over how their personal data is collected & sold.  

    • 🏥 HIPAA (Health Insurance Portability and Accountability Act – USA)  
      Governs protection of healthcare data (PHI).  
      Applies to hospitals, labs, insurers, and service providers.  

    • 💳 PCI DSS (Payment Card Industry Data Security Standard – Global)  
      Ensures safe handling of credit card/payment data.  

    • 📊 SOX (Sarbanes-Oxley Act – USA)  
      Focused on financial reporting integrity.  
      Requires data accuracy and auditability.  

---

## ✅ Compliance
    • Organizations must follow the above regulations if applicable.  

    • Consequences of non-compliance:  
        💸 Heavy fines (millions in some cases).  
        ⚖️ Legal action.  
        💔 Loss of customer trust.  
        📉 Business disruption or shutdown.  

---

## 🔄 Data Lifecycle (in Context of Governance & Compliance)

    • 📥 Acquisition  
      Collecting data ethically, with proper consent.  

    • ⚙️ Processing  
      Using data only for agreed, lawful purposes.  

    • 💾 Storage Stage  
      Securely storing data, enforcing access control & encryption.  

    • 🔗 Sharing Stage  
      Sharing with authorized parties only, with data contracts in place.  

    • 🗂️ Retention & Disposal  
      Keeping data only as long as necessary.  
      Proper erasure (secure deletion, anonymization) required.  

---

## 💻 Technology as an Enabler

    • 🔐 Authentication & Access Control  
      Role-based access, least privilege, multi-factor authentication.  

    • 🛡️ Encryption & Data Masking  
      Data at Rest → Encrypted databases, disk encryption.  
      Data in Transit → TLS/SSL, VPNs, secure APIs.  

    • ☁️ Hosting  
      Cloud platforms with built-in compliance certifications (AWS, GCP, Azure).  

    • 👀 Monitoring & Alerting  
      Track suspicious activity, detect breaches early, generate compliance logs.  

    • 🧹 Data Erasure (Software-Based)  
      Secure wipe tools or anonymization to ensure deleted data cannot be recovered.  

---

## 🔑 Summary
    • Data governance = rules + frameworks.  
    • Compliance = following those rules or facing consequences.  
    • Governance & compliance cover the entire data lifecycle (from acquisition → disposal).  
    • Technology (encryption, access control, monitoring) makes compliance achievable.  

---

# 🔄 DataOps Methodology

---

## 📌 Definition (Gartner)
    DataOps = Collaborative data management practice.  
    Goal → Improve communication, integration, and automation of data flows  
    between **data managers** and **data consumers** across the organization.  

    • Focus → Predictable delivery + change management of data, models, and artifacts.  
    • Uses automation to ensure → security, quality, metadata management, and efficiency.  

---

## 🏗️ Why DataOps?
    • Works well for small teams with simple use cases.  
    • As pipelines, infra, and teams grow → need structured processes.  
    • Helps govern the full **data + analytics lifecycle**:  
        - Ingestion → Processing → Analytics → Reporting.  
    • Reduces data defects, improves cycle times, ensures access to quality data.  

---

## ⚙️ How DataOps Works
    • Uses → Metadata management, workflow automation, test automation.  
    • Tools → Code repositories, collaboration platforms, orchestration.  
    • Ensures → Activities happen in the right order with proper security.  
    • Benefits → Automates processes, reduces waste, increases throughput.  

---

## 📚 DataOps Methodology (3 Phases)

    1️⃣ Establish DataOps Phase  
        • Set up org structure, governance, and best practices.  
        • Define standards for data management & pipelines.  

    2️⃣ Iterate DataOps Phase  
        • Deliver data for one sprint.  
        • Focused, incremental delivery of analytics & pipelines.  

    3️⃣ Improve DataOps Phase  
        • Apply learnings from sprints.  
        • Continuous improvement of processes, tools, and collaboration.  

---

## 🚀 Benefits of DataOps

    • 📂 Metadata & Catalog Automation  
      Automates metadata management, makes data assets easy to find.  

    • 🧭 Data Lineage  
      Trace where data came from → builds trust, ensures compliance.  

    • 🤖 Workflow Automation  
      Automates jobs in the data lifecycle → improves integrity, relevancy, security.  

    • ⚡ Streamlined Processes  
      Ensures faster, reliable access to data for business needs.  

    • 🔄 Business-Ready Pipelines  
      Data pipelines are always available for consumers & stakeholders.  

    • 🌐 Data-Driven Culture  
      Promotes trust in data through automation, quality checks, governance.  

    • 👨‍💻 For Data Practitioners  
        - Reduce development time.  
        - Cut waste & duplication.  
        - Increase productivity & throughput.  
        - Deliver higher-quality data consistently.  

---

## 🛠️ Popular DataOps Platforms
    • IBM DataOps  
    • Nexla  
    • Switchboard  
    • Streamsets  
    • Infoworks  

---

## 👨‍🔧 Career Angle: DataOps Engineer
    • Focuses on the **development + deployment lifecycle**, not just the product.  
    • Works on → defining data strategy, developing processes, establishing metrics.  
    • Role blends → engineering + governance + automation + collaboration.  
    • Growing demand → more career opportunities as orgs adopt DataOps.  

---

## 🔑 Summary
    • DataOps = Agile + DevOps mindset applied to data management.  
    • Helps orgs → reduce errors, accelerate delivery, improve trust in data.  
    • Uses → automation, orchestration, collaboration to govern the data lifecycle.  
    • Benefits → Faster insights, secure/reliable pipelines, stronger data culture.  

