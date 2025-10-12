# Topic: Module 1 — Introducing Relational Database Products

---

# 🧠 Database Architecture

## 💡 Deployment Topology

### 🏗️ Single-Tier Architecture
- The **database**, **application**, and **user interface** all exist on the same machine.  
- Common in personal database systems.

**Example:**  
A Microsoft Access database where you directly enter, store, and retrieve data on your own computer.

---

### 👥 Client-Server Architecture
- Divides work between two main layers:  
  - **Client Layer** – handles user interaction and sends requests.  
  - **Server Layer** – processes requests and manages the database.

#### 🔧 DBMS Layer (Server Side)
- **Data Access:** Manages how applications read/write data.  
- **Database Engine:** Executes queries and manages transactions.  
- **Database Storage:** Physically stores data on disk.  
- **Communication Interface:** Enables data exchange between client and database.

**Example:**  
A hospital management system where nurses (clients) access patient data stored on a central hospital server (server).

---

### 🧩 Three-Tier Architecture
- Adds a **middle (application)** layer between client and server.  
- Improves performance, scalability, and security.

**Tiers:**
1. **Client Tier** – user interface (browser or app).  
2. **Application Tier** – processes logic and connects to DB.  
3. **Database Tier** – stores and manages data.

**Example:**  
An online banking app:  
- You use the **mobile app** (client).  
- The bank’s **application server** processes your request.  
- The **database server** stores your transaction data.

---

### ☁️ Cloud-Based Architecture
- Database is hosted on a cloud platform (e.g., AWS, Azure, Google Cloud).  
- Offers scalability, remote access, and managed services.

**Example:**  
A company uses **Amazon RDS (Relational Database Service)** to host their MySQL database accessible from anywhere.

---

### ⚙️ Architecture Emergence Factors
- **Security Concern:** Sensitive data needs controlled access.  
- **Performance:** Distributed processing improves speed.  
- **Maintainability:** Easier to update or scale when tiers are separated.

---

✅ **Summary**

| Architecture    | Layers | Example               | Key Advantage        |
|-----------------|---------|-----------------------|----------------------|
| Single-Tier     | 1       | MS Access             | Simplicity           |
| Client-Server   | 2       | Hospital DB System    | Centralized Data     |
| Three-Tier      | 3       | Online Banking        | Secure & Scalable    |
| Cloud-Based     | Variable| AWS RDS               | Flexible & Global    |

---

# 🌐 Distributed Architecture and Clustered Databases

## 🏗️ Types of Database Architecture

### 💾 Shared Disk Architecture
- All nodes **share the same storage**, but each has its own processor and memory.  
- Each node can access the same database files through a common disk system.

**Advantages:**
- Easy to add or remove nodes.  
- Simplified data consistency since all nodes share one storage.  
- Good fault tolerance — if one node fails, others can continue.

**Disadvantages:**
- Disk contention (multiple nodes trying to access the same disk).  
- Requires high-speed interconnects for performance.  
- Scalability is limited by shared storage bandwidth.

**Example:**  
Oracle RAC (Real Application Clusters) uses a shared disk setup.

---

### 🧩 Shared Nothing Architecture
- Each node has its **own CPU, memory, and disk**.  
- Data is divided among nodes (no shared storage).

**Advantages:**
- High scalability — you can add more nodes easily.  
- No single point of contention for data access.  
- Excellent fault isolation (failure in one node doesn’t affect others).

**Disadvantages:**
- Complex data distribution and synchronization.  
- Load balancing can be difficult.  
- Harder to ensure global consistency.

**Example:**  
Google Spanner and Amazon Redshift use shared-nothing architecture.

---

### ⚙️ Combination and Specialized Architectures
- Mix elements of both **shared disk** and **shared nothing** designs.  
- May include hybrid or specialized clustering methods for specific workloads.

**Advantages:**
- Flexible — can be optimized for performance or reliability.  
- Balances between scalability and consistency.  
- Suitable for enterprise-level or hybrid cloud setups.

**Disadvantages:**
- More complex to configure and maintain.  
- Higher cost due to specialized hardware/software.  
- Requires careful tuning to avoid performance bottlenecks.

**Example:**  
IBM Db2 pureScale and some hybrid cloud databases use this approach.

---

## 🔁 Common Techniques in Distributed Databases

### 📀 Database Replication
- Copies data from one database to another to improve **availability** and **fault tolerance**.  
- Can be **synchronous** (real-time) or **asynchronous** (delayed).

**Example:**  
A company replicates its main database from Manila to Singapore for backup and faster local access.

---

### 🧱 Database Partitioning and Sharding
- **Partitioning:** Divides a single database into smaller, manageable segments.  
- **Sharding:** A form of horizontal partitioning — splits large tables across multiple servers.

**Benefits:**
- Improves query performance.  
- Enables parallel processing.  
- Makes scaling easier as data grows.

**Example:**  
A social media app shards its user database by region — Asia, Europe, and America — to reduce load on any single server.

---

✅ **Summary**

| Architecture Type         | Storage Model  | Example                | Main Advantage          | Main Disadvantage              |
|----------------------------|----------------|------------------------|--------------------------|--------------------------------|
| Shared Disk                | Common Storage | Oracle RAC             | Easy to manage consistency | Disk contention issues         |
| Shared Nothing             | Independent    | Google Spanner         | Highly scalable           | Complex synchronization        |
| Combination / Specialized  | Hybrid         | IBM Db2 pureScale      | Flexible and balanced     | Complex and costly setup       |

| Technique                  | Purpose                    | Example Use Case                                   |
|-----------------------------|-----------------------------|----------------------------------------------------|
| Database Replication        | Backup & High Availability  | Manila–Singapore mirrored databases                |
| Partitioning / Sharding     | Scalability & Performance   | Regional user database separation in social media  |

--- 

# 🧰 Database Usage Patterns

## 👤 Key User Roles
Databases are accessed by different types of users depending on their purpose and expertise.

- **Database Administrator (DBA):** Manages, secures, and maintains the database.  
  *Example:* Configures backups and user access permissions.  
- **Database Designer:** Creates the schema, defines tables, relationships, and constraints.  
  *Example:* Designs how patient records relate to doctor information.  
- **Application Developer:** Writes applications that interact with the database.  
  *Example:* Builds a hospital management system using SQL queries in the code.  
- **End User:** Interacts with data through applications or dashboards.  
  *Example:* A nurse retrieves a patient’s lab result using the hospital app.

---

## 🖥️ Graphical User Interfaces (GUIs)
GUIs allow users to interact with databases visually — no coding required.

**Features:**
- Drag-and-drop table views  
- Query builders and data visualizations  
- Easier data inspection and editing

**Examples:**
- phpMyAdmin for MySQL  
- pgAdmin for PostgreSQL  
- SQL Server Management Studio (SSMS) for Microsoft SQL Server

**Use Case:**  
An analyst views and filters patient data without writing SQL commands.

---

## 💻 Command-Line Interfaces (CLIs)
CLIs let users manage and query databases using typed commands — fast and scriptable.

**Advantages:**
- Lightweight and flexible  
- Can automate tasks via scripts  
- Preferred by developers and DBAs for advanced control

**Examples:**
- `mysql` command line  
- `psql` (PostgreSQL)  
- `sqlcmd` (SQL Server)

**Use Case:**  
A DBA executes a batch of SQL scripts to update hospital records overnight.

---

## 🔗 Application Programming Interfaces (APIs)
APIs enable **programs to interact with databases** without direct SQL queries.  
Applications send requests through an API, which handles data exchange.

**Advantages:**
- Security — limits direct database access  
- Easier integration with apps and web services  
- Enables remote or cloud-based database access

**Examples:**
- RESTful APIs using HTTP requests  
- Python’s `sqlite3` or `SQLAlchemy` libraries  
- Java’s JDBC (Java Database Connectivity)

**Use Case:**  
A web app fetches patient appointment data via an API instead of connecting directly to the database.

---

## 🧩 Object-Relational Mapping (ORM)
ORM bridges the gap between **object-oriented programming** and **relational databases**.  
It converts objects in code into database records automatically.

**Advantages:**
- No need to write raw SQL queries  
- Simplifies database operations  
- Increases code maintainability

**Disadvantages:**
- Can reduce performance for complex queries  
- Limited control over low-level SQL

**Examples:**
- Python → SQLAlchemy, Django ORM  
- Java → Hibernate  
- C# → Entity Framework

**Use Case:**  
A developer uses Django ORM to store and retrieve patient information in a PostgreSQL database through Python classes instead of SQL.

---

✅ **Summary**

| Component / Concept | Description / Role                                 | Example Tools or Use Case                             |
|----------------------|----------------------------------------------------|--------------------------------------------------------|
| Key User Roles       | DBAs, designers, developers, and end users         | DBA maintaining hospital database                     |
| GUI                  | Visual interface for managing data                 | phpMyAdmin, pgAdmin, SSMS                             |
| CLI                  | Text-based command interface                       | mysql, psql, sqlcmd                                   |
| API                  | Programmatic access for applications               | REST API, Python `sqlite3`                            |
| ORM                  | Maps objects in code to database tables            | SQLAlchemy, Hibernate, Django ORM                     |
