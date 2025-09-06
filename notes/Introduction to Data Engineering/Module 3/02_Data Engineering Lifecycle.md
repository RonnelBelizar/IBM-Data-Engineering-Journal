# Topic: Module 3 - Data Engineering Lifecycle

---

# 📥 Gathering and Importing Data

---

## 1. SQL (Relational Databases)
    • Pull data using SQL queries (SELECT, JOIN, WHERE).  
    • Often used for structured data in RDBMS (MySQL, PostgreSQL, Oracle).  
    • Destination → Data Warehouse, Data Lake, or another SQL DB.  

---

## 2. Non-Relational Databases (NoSQL)
    • Extract data from document, key-value, columnar, or graph stores.  
    • Use APIs, drivers, or query languages (e.g., MongoDB queries, Cassandra CQL).  
    • Destination → Data Lake or another NoSQL DB.  

---

## 3. APIs (Application Programming Interfaces)
    • Systems expose endpoints to request data (REST, GraphQL, SOAP).  
    • Often returns JSON or XML.  
    • Good for external data (weather, finance, healthcare APIs).  
    • Destination → Databases, Warehouses, or Data Pipelines.  

---

## 4. Web Scraping
    • Extract data directly from websites (HTML parsing).  
    • Tools: BeautifulSoup, Scrapy, Selenium.  
    • Caution: Legal/ethical considerations (respect robots.txt, terms).  
    • Destination → NoSQL DBs, CSV/JSON files, Data Lake.  

---

## 5. Sensor Data (IoT, Medical Devices)
    • Real-time streams from devices (IoT sensors, patient monitors, lab machines).  
    • Protocols: MQTT, OPC-UA, proprietary vendor APIs.  
    • Destination → Data Lake, Time-series DB (e.g., InfluxDB), or Streaming Platform (Kafka).  

---

## 6. Data Exchange Platforms
    • Marketplaces and hubs for bulk datasets (open data portals, Kaggle, gov data).  
    • Typically downloaded in CSV, JSON, or Excel.  
    • Destination → Warehouses, Data Lakes.  

---

## 7. Other Sources
    • Files → CSV, XLSX, JSON, XML, Parquet.  
    • Logs → Application/system logs (useful for monitoring + analytics).  
    • Emails → Extract structured + unstructured info from messages.  

---

## 8. Data Types and Destinations
    • Structured → SQL DBs, Warehouses.  
    • Semi-structured → NoSQL DBs, Data Lakes.  
    • Unstructured → Data Lakes, Object Storage (S3, GCS, Azure Blob).  
    • Real-time Streams → Message Queues (Kafka, RabbitMQ), then processed into Warehouses or Lakes.  

---

## 🔑 Summary
    • Data can come from databases (SQL/NoSQL), APIs, scraping, sensors, or exchanges.  
    • Choice depends on source type, format, and business need.  
    • Destination varies: DBs for transactions, Warehouses for analytics, Data Lakes for raw/unstructured, Streams for real-time.  

---

# 🧹 Data Wrangling / Munging

---

## 📝 What is Data Wrangling?
    • Process of taking raw, messy, or scattered data and turning it into a clean, structured, and usable form.  
    • Goal → Make data ready for analysis, reporting, or machine learning.  
    • Why? → Raw data is often incomplete, inconsistent, or in the wrong format.  
    • Think of it as: "taming wild data so it can work for you."  

---

## 1. Exploration
    • First step: understand the data before changes.  
    • Inspect data types, size, and distributions.  
    • Tools → Pandas (Python), SQL queries, BI tools.  
    • Example → Look at patient lab records: column types, missing values, outliers.  

---

## 2. Transformation
    • Goal: convert raw data into usable formats.  

    🔹 Structuring  
        - Joins → Combine data across tables (e.g., patient info + test results).  
        - Unions → Stack datasets with same schema (e.g., monthly logs).  

    🔹 Normalization  
        - Organize into smaller related tables to reduce redundancy.  
        - Example: Split patient demographic info from test results.  

    🔹 Denormalization  
        - Merge tables for faster reads/analytics.  
        - Example: Combine all patient info + lab results into one wide table for reporting.  

---

## 3. Cleaning
    • Fix errors, handle missing values, and standardize.  

    🔹 Inspection  
        - Data Profiling → Stats about columns (min, max, null counts, unique values).  
        - Visualizing → Graphs to spot trends/anomalies (e.g., boxplot for outliers).  

    • Example → Fix misspelled hospital names, remove duplicate patient IDs.  

---

## 4. Validation
    • Ensures transformed/cleaned data meets rules + expectations.  
    • Examples:  
        - Dates must be valid (no Feb 30).  
        - IDs unique per patient.  
        - No negative ages.  
    • Tools → Great Expectations, Pandera, custom scripts.  

---

## 5. Availability
    • Make processed data accessible to end-users/systems.  
    • Load into destination → Warehouse, Lake, Dashboard, or API.  
    • Ensures proper permissions + uptime.  
    • Example → Publish cleaned GX device data into a BI dashboard for hospitals.  

---

## 🔑 Summary
    • Wrangling = Exploration → Transformation → Cleaning → Validation → Availability.  
    • Joins/unions, normalization/denormalization shape the structure.  
    • Profiling + visualization help find issues before processing.  
    • Final data must be both clean and available for use.  

---

💡 Bonus:  
    • 80% of a data engineer’s time often goes to wrangling/cleaning.  
    • Automation (ETL/ELT pipelines, validation frameworks) reduces manual work.  
    • Good wrangling = faster analytics + reliable insights.  

---

# 🛠️ Tools for Data Wrangling

---

## 1. Spreadsheets / Low-Code Tools
    • Excel Power Query / Google Sheets  
        - Easy entry point for small datasets.  
        - Drag-and-drop transforms, filtering, joining.  
        - Why use → Familiar, quick for ad-hoc cleaning.  
        - Why not → Limited scalability, not great for big data.  

---

## 2. OpenRefine
    • Open-source tool for cleaning messy data.  
    • Great for reconciling inconsistent entries (e.g., “NYC” vs “New York City”).  
    • Why use → Strong for text-heavy, dirty datasets.  
    • Why not → More manual than automated pipelines.  

---

## 3. Google DataPrep (by Trifacta)
    • Cloud-based wrangling tool, tightly integrated with GCP.  
    • Smart suggestions for cleaning + transforming data.  
    • Why use → Good for cloud-native teams.  
    • Why not → Paid tool, tied to Google Cloud.  

---

## 4. Watson Studio Refinery
    • IBM’s data prep environment, integrated into Watson Studio.  
    • Helps prep data for ML/AI workflows.  
    • Why use → Good if you’re in IBM ecosystem.  
    • Why not → Proprietary, may be heavy for simple tasks.  

---

## 5. Trifacta Wrangler
    • Advanced wrangling platform (basis for Google DataPrep).  
    • Visual + code-based data prep for analysts/engineers.  
    • Why use → Automates repetitive cleaning steps, scales well.  
    • Why not → Commercial product, not free.  

---

## 6. Python (Coding Approach)
    • Jupyter Notebook → Interactive coding + exploration.  
    • NumPy → Fast math, array manipulation.  
    • Pandas → Core library for data cleaning, joining, transforming.  
    • Why use → Flexible, powerful, scalable with other libraries.  
    • Why not → Requires coding knowledge.  

---

## 7. R (Coding Approach)
    • dplyr → Grammar of data manipulation (filter, group, join).  
    • data.table → High-performance data manipulation.  
    • jsonlite → Handle JSON data easily.  
    • Why use → Built for statistics + visualization.  
    • Why not → Less common in data engineering pipelines than Python.  

---

## 🔑 Summary
    • Non-coding tools (Excel, OpenRefine, Trifacta) → Great for beginners + smaller projects.  
    • Cloud/proprietary tools (Google DataPrep, Watson Refinery) → Strong for enterprise workflows.  
    • Python + R → Most flexible + scalable for engineers and data scientists.  
    • Choice depends on → dataset size, complexity, and your workflow.  

---


