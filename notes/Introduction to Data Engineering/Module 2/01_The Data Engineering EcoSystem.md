# Topic: Module 2 - The Data Engineering Ecosystem

---

## 1. Types of Data
    • Structured  
        - Organized in strict rows/columns.  
        - Easy to query and store in RDBMS.  
        - Example: Excel spreadsheets.  

    • Semi-structured  
        - Partially organized, flexible schema.  
        - Uses tags/keys for structure.  
        - Examples: JSON, XML, Emails (headers vs body).  

    • Unstructured  
        - No fixed schema, free-form data.  
        - Examples: Images, Videos, PDFs, Social posts.  

---

## 2. Sources of Data
    • Relational Databases → MySQL, PostgreSQL.  
    • Non-relational Databases → MongoDB, Cassandra.  
    • APIs → Request/response to external systems.  
    • Web Services → SOAP, REST.  
    • Data Streams → IoT sensors, stock market feeds.  
    • Social Platforms → Facebook, Twitter, Instagram.  
    • Sensor Devices → Medical equipment, IoT devices.  

---

## 3. Data Repositories
    • Transactional (OLTP)  
        - Real-time operations (deposits, orders).  
        - Example: ATM recording transactions.  

    • Analytical (OLAP)  
        - Analyzes historical data.  
        - Example: Sales trend analysis.  

---

## 4. Data Flow
    • Data Integration → Collect → Clean → Transform → Deliver.  
    • Data Pipeline → Automates movement from source → destination.  
        - Example: Extract DB → Transform → Load into warehouse.  
    • BI Tools → Visualize data.  
        - Examples: Power BI, Tableau, Looker.  

---

## 5. File Formats
    • Delimited Text → CSV, TSV.  
        - Example: `name,age,city`.  
    • XLSX → Excel workbook (sheets, formulas).  
    • XML → Tagged structure.  
        - Example: `<user><name>John</name></user>`.  
    • PDF → Fixed layout (e.g., scanned reports).  
    • JSON → Lightweight structured format.  
        - Example: `{ "name": "Alice", "age": 25 }`.  

---

## 6. Programming Languages for Data
    • SQL → Query/manipulate RDBMS.  
    • Python → Pandas (clean), NumPy (math), Matplotlib (viz), Scrapy (scraping), OpenCV (images).  
    • R → Statistics + visualization.  
    • Java → General-purpose, scalable apps.  
    • Unix/Linux Shell → Automate scripts/jobs.  
    • PowerShell → Windows scripting, works with JSON/CSV/APIs.  

---

## 7. Metadata ("Data about Data")
    • Technical Metadata → Defines structures (tables, columns, datatypes).  
        - Example: Schema.  
    • Process Metadata → Tracks data jobs/performance.  
        - Example: ETL job log.  
    • Business Metadata → Business meaning/context.  
        - Example: Defines “revenue.”  
    • Management → Policies + tools (Data Catalog).  

    🔧 Tools → IBM InfoSphere, Oracle Builder, Talend, Azure Data Catalog, Watson Catalog, Alation, Informatica.  

---

## 8. Data Repositories (Expanded)
    ### 8.1 Databases  
        • Managed by DBMS → Handles querying, security, transactions.  

        ✅ Factors: Data type, structure, query style, latency, speed.  

        🔹 Relational (RDBMS) → Tabular, SQL-based.  
            - Examples: MySQL, PostgreSQL, Oracle, SQL Server.  

        🔹 Non-relational (NoSQL) → Flexible, scalable.  
            - Document → MongoDB, CouchDB.  
            - Key-Value → Redis, DynamoDB.  
            - Column → Cassandra, HBase.  
            - Graph → Neo4j.  

    ### 8.2 Data Warehouse (DW)  
        • Consolidated, cleaned data for analysis.  
        • Optimized for OLAP.  
        • ETL Process → Extract → Transform → Load.  
        - Examples: Redshift, BigQuery, Snowflake, Synapse.  

    ### 8.3 Big Data Stores  
        • Handle very large-scale distributed data.  
        - Examples: Hadoop HDFS, Cassandra, Google Bigtable.  

    ### 8.4 Data Lakes  
        • Store raw structured + unstructured data.  
        • Cheap + flexible but can get messy.  
        - Examples: AWS S3, Azure Data Lake, GCS.  

---

## 🔑 Summary (Data Engineering Context)
    • Data = structured, semi-structured, unstructured.  
    • Sources = DBs, APIs, streams, sensors, social media.  
    • Repositories = Databases, Warehouses, Big Data Stores, Lakes.  
    • Pipelines = Move + transform data for BI tools.  
    • File formats = CSV, JSON, XML, PDF, Excel.  
    • Programming = SQL, Python, R, Java, Shell, PowerShell.  
    • Metadata = Context + structure; managed via catalogs.  
    • Choice of system = Impacts scalability, cost, performance.  

---

# Relational Database Management System (RDBMS)

## 📝 What is RDBMS?
    • RDBMS = Relational Database Management System  
    • A software that stores data in **tables** (rows & columns).  
    • Think of it like **Excel**, but more powerful and can connect multiple tables together.  

---

## ✅ Why is it Used?
    • To organize large amounts of structured data (with clear rows/columns).  
    • Ensures data is consistent and accurate (via rules like Primary Key & Foreign Key).  
    • Allows easy data retrieval using SQL (Structured Query Language).  
    • Great when relationships between data matter (e.g., patients ↔ medical records).  

---

## ❌ Why Not (Limitations)?
    • Not flexible for unstructured data (like images, logs, IoT data).  
    • Scaling can be expensive and complex (big data is harder in RDBMS).  
    • Fixed schema → changing structure later can be difficult.  
    • Better for **OLTP (transactions)** than for **Big Data analytics**.  

---

## 👍 Pros
    • Enforces ACID properties → reliable transactions.  
    • Data integrity & security.  
    • Easy to use with SQL (universal query language).  
    • Supports relationships between tables.  

## 👎 Cons
    • Less flexible for unstructured or semi-structured data.  
    • Can be slower with very large datasets compared to NoSQL.  
    • Vertical scaling (adding CPU/RAM) is costly.  
    • Rigid schema design → less agile for changing data needs.  

---

## 💻 Examples of RDBMS Software
    • MySQL → Open-source, widely used in web applications.  
    • PostgreSQL → Open-source, advanced features, very reliable.  
    • Oracle Database → Enterprise-grade, powerful but expensive.  
    • Microsoft SQL Server → Popular in businesses, integrates with Microsoft tools.  
    • IBM Db2 → IBM’s RDBMS, strong for enterprise & big workloads.  

---

## 📊 RDBMS in Data Engineering
    • Acts as a **source of truth** → where clean, structured data is first stored.  
    • Used in **ETL pipelines** to extract data before moving it to warehouses/lakes.  
    • Healthcare, finance, retail, and most traditional industries rely on it.  
    • Works best for **structured, relational data** (tables with clear rules).  

---

## 🔑 Summary
    • RDBMS = Stores and manages data in tables.  
    • Great for structured, relational data.  
    • Strong in consistency, integrity, and reliability.  
    • Weak in handling massive unstructured/big data.  


# NoSQL (Not Only SQL)

## 📝 What is NoSQL?
    • NoSQL = "Not Only SQL" (a type of database, not limited to tables).  
    • Designed to handle **unstructured, semi-structured, or very large-scale data**.  
    • Instead of strict tables, it stores data in flexible formats like:  
        - Key-Value pairs  
        - Documents (JSON-like)  
        - Wide-Column stores  
        - Graphs  

---

## 🔄 Types of NoSQL Databases
    • Key-Value Store  
        - Data stored as key + value (like a dictionary in Python).  
        - Super fast, great for caching and quick lookups.  
        - Example: Redis, DynamoDB  

    • Document Store  
        - Data stored as documents (usually JSON-like).  
        - Flexible schema → different documents can have different fields.  
        - Example: MongoDB, CouchDB  

    • Wide-Column Store  
        - Stores data in rows and dynamic columns.  
        - Scales to billions of rows across servers.  
        - Example: Cassandra, HBase  

    • Graph Database  
        - Stores data as nodes and relationships (edges).  
        - Perfect for networks, recommendations, and connected data.  
        - Example: Neo4j, ArangoDB  

---

## ✅ Why is it Used?
    • Works well for **Big Data** and **real-time applications**.  
    • Can handle unstructured data → logs, sensor data, images, JSON, etc.  
    • Flexible schema → you don’t need to define structure before storing data.  
    • Scales easily across many servers (horizontal scaling).  

---

## ❌ Why Not (Limitations)?
    • Not always ACID-compliant (sometimes sacrifices consistency for speed).  
    • Querying is less standardized (SQL is universal, NoSQL varies per database).  
    • Less ideal for highly relational data (where you need strong links between tables).  
    • Some NoSQL systems trade accuracy for availability & performance.  

---

## 👍 Pros
    • Flexible → no fixed schema.  
    • Great for handling **huge volumes** of diverse data.  
    • Scales horizontally (add more servers instead of just upgrading one).  
    • Works well for real-time and distributed systems.  

## 👎 Cons
    • Weaker data consistency compared to RDBMS.  
    • No single query language standard (varies per system).  
    • Can be complex to manage for certain workloads.  
    • Less suited for strong relational data models.  

---

## 💻 Examples of NoSQL Databases
    • MongoDB → Document-based, very popular, JSON-style.  
    • Cassandra → Wide-column, great for huge datasets, used by big companies.  
    • Redis → Key-Value store, very fast, often used for caching.  
    • Neo4j → Graph database, used for networks & relationships (e.g., social media).  
    • CouchDB → Document-based, stores JSON and syncs easily.  

---

## 📊 NoSQL in Data Engineering
    • Useful when working with **unstructured or fast-changing data**.  
    • Common in Big Data pipelines, IoT, and real-time analytics.  
    • Complements RDBMS (they are often used together in modern systems).  
    • Supports scenarios where scalability and speed matter more than strict consistency.  

---

## 🔑 Summary
    • NoSQL = Flexible databases for unstructured and large-scale data.  
    • 4 main types: Key-Value, Document, Wide-Column, Graph.  
    • Best for scalability, speed, and real-time apps.  
    • Not ideal when strong consistency and complex relationships are required.  
    • Works alongside RDBMS in modern data engineering.  

# RDBMS vs NoSQL

| Feature                 | RDBMS (Relational DB)                                      | NoSQL (Not Only SQL)                             |
|-------------------------|------------------------------------------------------------|--------------------------------------------------|
| **Data Structure**      | Tables (rows & columns)                                    | Key-Value, Document, Wide-Column, Graph          |
| **Schema**              | Fixed, predefined schema                                   | Flexible / dynamic schema                        |
| **Relationships**       | Strong support (Primary Key, Foreign Key)                  | Limited (only Graph DB handles this well)        |
| **Query Language**      | SQL (universal and standardized)                           | Varies (Mongo Query, CQL, etc.)                  |
| **Scalability**         | Vertical (add more CPU/RAM to one server)                  | Horizontal (add more servers/nodes)              |
| **Best For**            | Structured, relational data                                | Unstructured or semi-structured, large-scale     |
| **Consistency**         | Strong (ACID properties)                                   | Often weaker (many use BASE model)               |
| **Performance**         | Great for transactions and small/medium datasets           | Great for Big Data and real-time applications    |
| **Examples**            | MySQL, PostgreSQL, Oracle, SQL Server, IBM Db2             | MongoDB, Cassandra, Redis, Neo4j, CouchDB        |
| **Use Case**            | Banking, healthcare, ERP, enterprise systems               | Social media, IoT, analytics, recommendation     |

---

## 🔑 Quick Takeaway
    • Use **RDBMS** when: data is structured, relationships matter, consistency is critical.  
    • Use **NoSQL** when: data is massive, unstructured, or requires speed and scalability.  
    • In modern systems → they are often used together!  


---

# Data Warehouse, Data Mart, Data Lake

## 🏢 Data Warehouse (DW)
    • Central storage for **structured, cleaned, and processed data**.  
    • Stores data from multiple sources (databases, apps, logs).  
    • Optimized for **analytics and reporting**, not for daily transactions.  
    • Uses SQL for querying.  
    • Example: Amazon Redshift, Google BigQuery, Snowflake.  

    ✅ Why use it?  
        - To analyze company-wide data.  
        - Ensures data is consistent and trustworthy.  
        - Powers BI dashboards and reports.  

    ❌ Limitations  
        - Expensive for very large datasets.  
        - Mostly handles structured data (tables).  

    🔄 Types of Data Warehouses  
        • Enterprise Data Warehouse (EDW) → central store for the whole company.  
        • Operational Data Store (ODS) → near real-time updates, good for day-to-day decisions.  
        • Cloud Data Warehouse → hosted on cloud providers (e.g., BigQuery, Snowflake, Redshift).  

---

## 🛒 Data Mart
    • A **subset of a Data Warehouse**, focused on a specific department or use case.  
    • Example:  
        - Finance Data Mart → only finance-related data.  
        - Sales Data Mart → only sales data.  
    • Lighter and easier to query than the full Data Warehouse.  

    ✅ Why use it?  
        - Faster, easier access for specific teams.  
        - Avoids overwhelming users with all company data.  

    ❌ Limitations  
        - Limited scope → not useful for cross-department analysis.  
        - Needs to be updated from the Data Warehouse.  

    🔄 Types of Data Marts  
        • Dependent → built from a Data Warehouse (most common).  
        • Independent → standalone, not linked to a Data Warehouse.  
        • Hybrid → combines both approaches.  

---

## 🌊 Data Lake
    • A storage system that keeps **raw data in its original format**.  
    • Can hold **structured, semi-structured, and unstructured data**.  
    • Example: CSV, JSON, images, videos, logs, sensor data.  
    • Scalable and cheap (often on cloud storage).  

    ✅ Why use it?  
        - Flexible: store *everything*, even messy data.  
        - Prepares data for later processing into DW.  
        - Great for Big Data and Machine Learning projects.  

    ❌ Limitations  
        - Data can be messy → "data swamp" if not organized.  
        - Harder for business users to query directly.  

    🔄 Types of Data Lakes  
        • Raw Data Lake → stores unprocessed, original data.  
        • Processed Data Lake → stores cleaned and structured data.  
        • Cloud Data Lake → managed service (e.g., AWS S3, Azure Data Lake, GCP Cloud Storage).  

---

## 🔗 How They Relate
    • Data Lake → stores **raw, all types of data** (cheap, flexible).  
    • Data Warehouse → stores **processed, structured, clean data** (good for analytics).  
    • Data Mart → a **smaller slice** of the Data Warehouse for a specific department.  

    Example Flow:  
        1. Collect raw GX data (CSV, logs, reports) → Data Lake.  
        2. Clean, transform, aggregate → Data Warehouse.  
        3. Provide a smaller view for Finance or Service Team → Data Mart.  

---

## 🔑 Summary
    • Data Lake = Raw, messy storage (cheap, flexible, all data types).  
    • Data Warehouse = Structured, cleaned storage (analytics-ready).  
    • Data Mart = Small piece of a Data Warehouse (department-focused).  
    • Together → they form the modern data ecosystem.  

---

## 🏠 Data Lakehouse
    • A newer architecture that **combines features of Data Lakes and Data Warehouses**.  
    • Stores raw data like a Data Lake, but also supports structured queries like a Data Warehouse.  
    • Main idea → you don’t need separate systems anymore.  

    ✅ Why use it?  
        - Cheaper than a full Data Warehouse (uses Data Lake storage).  
        - Flexible: can handle structured + unstructured data.  
        - Reduces "data movement" → no need to copy from Lake → Warehouse.  
        - Great for both BI (business intelligence) and AI/ML use cases.  

    ❌ Limitations  
        - Still an evolving technology (younger than DW and DL).  
        - Not all companies/tools fully support it yet.  
        - May be complex to set up compared to traditional systems.  

    🔄 Examples of Data Lakehouse Platforms  
        • Databricks Lakehouse Platform  
        • Apache Iceberg (open-source)  
        • Delta Lake (open-source, by Databricks)  
        • Snowflake (adding lakehouse-style features)  

---

## 🔗 Where It Fits
    • Data Lakehouse tries to **merge the best of both worlds**:  
        - From Data Lake → raw, cheap, scalable storage.  
        - From Data Warehouse → reliable, structured querying with SQL.  

    • Some organizations now skip building separate DW + DL and go straight to Lakehouse.  
