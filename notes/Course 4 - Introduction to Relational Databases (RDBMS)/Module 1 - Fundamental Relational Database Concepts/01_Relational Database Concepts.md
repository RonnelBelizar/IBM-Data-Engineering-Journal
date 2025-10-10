# Topic: Module 1 — Relational Database Concepts

---

# 📘 Information and Data Models

Information and data models are frameworks that define how data is represented, managed, and related within a system.

---

## Data Management
The process of collecting, storing, organizing, and maintaining data efficiently and securely throughout its lifecycle.

---

## Information Model
An information model defines the meaning, context, and relationships of data. It focuses on how information is understood conceptually rather than how it is stored.

Aspects:
- Represents real-world entities and their relationships  
- Focuses on meaning and semantics  
- Used for business and analytical understanding  

---

## Data Model
A data model defines how data is structured, stored, and accessed within a database. It provides the blueprint for database design and implementation.

Aspects:
- Focuses on data representation and storage  
- Used for database implementation and design  

Schema:
Defines how data is logically organized in the database.  

Tables:
Hold data in rows and columns.  

Columns:
Represent attributes or fields within a table.  

Data Types:
Define the kind of data a column can store (e.g., INTEGER, TEXT, DATE).  

Indexes:
Improve the speed of data retrieval operations.

---

## Differences Between Information and Data Models

Level of Detail:  
- Information model is high-level and conceptual.  
- Data model is detailed and technical.  

Purpose:  
- Information model defines meaning and context.  
- Data model defines structure and storage.  

Usage:  
- Information model is used by analysts and stakeholders.  
- Data model is used by developers and database administrators.  

System Development:  
- Information model guides early design.  
- Data model implements the database structure.

---

## Hierarchical Model
A data model where data is organized into a tree-like structure with parent-child relationships, representing one-to-many relationships.

---

## Types of Data Models
Relational Model: Stores data in tables connected by keys.  
Entity-Relationship Model: Uses entities, attributes, and relationships to represent data.

---

## Converting ER Diagram into Tables
1. Each entity becomes a table.  
2. Each attribute becomes a column.  
3. Primary keys uniquely identify records.  
4. Foreign keys define relationships between tables.

---

## Simplified ER Diagram
STUDENT (Student_ID, Name, Age)  
COURSE (Course_ID, Title)  
ENROLLMENT (Student_ID, Course_ID)

Relationships:  
A student can enroll in many courses, and a course can have many students.

---

## Concepts in Database Management
Logical Data Independence: Ability to modify the logical schema without affecting applications.  
Physical Data Independence: Ability to change how data is stored physically without altering the logical schema.  
Physical Storage Independence: The separation of physical storage methods from logical data structures.

---

# 🧩 ENTITY-RELATIONSHIP DIAGRAMS (ERDs) AND TYPES OF RELATIONSHIPS

An **Entity-Relationship Diagram (ERD)** is a visual representation of how data entities relate within a system. It helps organize data logically and serves as a blueprint for database design.

🧠 ERD DEFINITION  
An ERD shows entities (tables), their attributes (fields), and how they connect through relationships. It clarifies how information flows through a database and identifies dependencies.

⚙️ FUNDAMENTAL COMPONENTS  
🟦 ENTITIES — Represent objects or concepts that data is stored about. Each entity becomes a database table, and its attributes become columns.  
Example:  
+-------------+  
|   PATIENT   |  
+-------------+  
| Patient_ID  |  
| Name        |  
| Age         |  
| Address     |  
+-------------+  

🟩 RELATIONSHIP SETS — Define how entities interact with each other. These show the logical associations between data in different tables.  
Example:  
+-----------+           +-----------+  
|  DOCTOR   |           |  PATIENT  |  
+-----------+           +-----------+  
| Doctor_ID |<--------->| Patient_ID|  
| Name      |  treats   | Name      |  
+-----------+           +-----------+  

🪶 CROW’S FOOT NOTATIONS — Used to represent **cardinality**, or how many instances of one entity relate to another.  
O---| → Zero or One  
|---| → Exactly One  
|---< → One to Many  
O---< → Zero to Many  
Examples:  
A patient may or may not have insurance → O---|  
Each invoice must belong to one customer → |---|  
A doctor can treat many patients → |---<  
A student may enroll in many courses → O---<  

🔄 TYPES OF RELATIONSHIPS  

1️⃣ ONE-TO-ONE (1:1)  
Each record in one entity corresponds to exactly one record in another. Common for optional or sensitive data stored separately.  
Example: A patient has one medical record.  
+-------------+      ||────||      +-----------------+  
|   PATIENT   |--------------------|  MEDICAL_RECORD |  
+-------------+                   +-----------------+  
| Patient_ID  |                   | Record_ID       |  
| Name        |                   | Patient_ID (FK) |  
+-------------+                   +-----------------+  

2️⃣ ONE-TO-MANY (1:N)  
One record in an entity can be related to multiple records in another. This is the most common type of relationship.  
Example: A doctor can treat many patients, but each patient has only one doctor.  
+-----------+        ||────<        +-----------+  
|  DOCTOR   |----------------------|  PATIENT  |  
+-----------+                     +-----------+  
| Doctor_ID |                     | Patient_ID|  
| Name      |                     | Doctor_ID (FK)|  
+-----------+                     +-----------+  

3️⃣ MANY-TO-MANY (M:N)  
Records in both entities relate to multiple records in the other. This requires a **junction table** to connect them.  
Example: A student can enroll in many courses, and a course can have many students.  
+-----------+        <───||───>        +-----------+  
|  STUDENT  |--------------------------|  COURSE   |  
+-----------+                         +-----------+  
| Student_ID|                         | Course_ID |  
| Name      |                         | Title     |  
+-----------+                         +-----------+  
          \                             /  
           \                           /  
            \                         /  
             \                       /  
              \                     /  
               \                   /  
                \                 /  
                 \               /  
                  \             /  
                   \           /  
                    \         /  
                     \       /  
                      \     /  
                       \   /  
                        \ /  
                 +----------------+  
                 |   ENROLLMENT   |  
                 +----------------+  
                 | Student_ID (FK)|  
                 | Course_ID  (FK)|  
                 +----------------+  

🧭 QUICK SUMMARY  
Entity → Table representing data objects  
Attribute → Column describing properties  
Relationship → Connection between entities  
Crow’s Foot → Symbol for relationship type  
1:1 → One record to one record (||----||)  
1:N → One record to many records (||----<)  
M:N → Many records to many records (<----||---->)  

✨ In summary, ERDs are blueprints for databases — they simplify complex data relationships, improve organization, and ensure data integrity.

---

# 🗂️ Mapping Entities to Tables

Mapping entities from an ERD to actual database tables can be straightforward if we follow some clear steps. Let's make it fun and easy! 😎

---

## 1️⃣ Begin with an ERD
- Start by looking at your **Entity-Relationship Diagram (ERD)** 🖼️.
- Identify:
  - **Entities** → Things or objects, like `Customer`, `Order`, `Product` 🧑‍💼📦
  - **Attributes** → Properties of entities, like `Customer Name`, `Order Date`, `Product Price` 📝
  - **Relationships** → How entities are connected, e.g., a `Customer` places an `Order` 🔗
- Think of ERD as your **map** 🗺️ before you build the database.

**Example:**
- Entity: `Customer`
- Attributes: `CustomerID`, `Name`, `Email`
- Relationship: `Customer` → `Order`

---

## 2️⃣ Map the ERD
- Turn each **entity** into a **table** 🏗️.
- Each **attribute** becomes a **column** in the table.
- Define **relationships** using **foreign keys** 🔑.
  
**Example Table: `Customer`**
| Column       | Data Type | Notes                    |
|--------------|-----------|--------------------------|
| CustomerID   | INT       | Primary Key, unique 🔑    |
| Name         | VARCHAR   | Customer's full name     |
| Email        | VARCHAR   | Customer's email address |

**Relationship Example:**  
- `Order.CustomerID` → foreign key referencing `Customer.CustomerID`

---

## 3️⃣ Translating Attributes
- Choose the correct **data type** for each attribute 🎯.
- Ensure it fits the data you want to store:
  - `INT` → numbers (e.g., quantity, age) 🔢
  - `VARCHAR` → text (e.g., names, emails) ✉️
  - `DATE` → dates (e.g., order date) 📅
- Decide if the attribute can be **NULL** or must always have a value ❌🟢

---

## 4️⃣ Adding Data Values
- Start populating your tables with **real data** 🏋️‍♂️
- Make sure the values match the **data type** of each column.
- Examples:
  - `CustomerID = 1`
  - `Name = "Ronnel Belizar"`
  - `Email = "ronnel@example.com"`

---

## 5️⃣ Best Practices ✅
### 🔹 Primary Key Designation
- Each table should have a **unique identifier** 🔑
- Example: `CustomerID` for `Customer` table

### 🔹 Data Validation
- Ensure **accuracy** of the data ✅
- Example: Emails should contain `@`, prices should not be negative 💡

### 🔹 Default Values
- Pre-set **default values** when applicable 🎯
- Example: `OrderStatus = "Pending"` if not specified

### 🔹 Using Views
- Simplify queries with **views** 👀
- Example: `CREATE VIEW ActiveCustomers AS SELECT * FROM Customer WHERE Status='Active'`

### 🔹 Concurrency Control
- Manage simultaneous **access and modifications** to the database 🔄
- Prevents conflicts when multiple users work on the same data 💻👥

---

## 📌 Summary
- Start with your ERD 🖼️ → entities, attributes, relationships
- Map entities to tables 🏗️ → columns, data types, foreign keys
- Translate attributes 🎯 → choose proper data types
- Add data values 🏋️‍♂️ → make sure they're valid
- Follow best practices ✅ → primary keys, validation, defaults, views, concurrency

By following these steps, you can easily turn an ERD into a clean, well-structured database! 🚀

--- 

# 🗃️ Data Types in Databases

Understanding **data types** is key to organizing your database efficiently. Let's break it down in a simple, fun way! 😎

---

## 1️⃣ Database Table Basics
- A **table** is made up of **columns** and **rows**.
- Each column has a **data type**, which tells the database what kind of data can be stored there 🏗️.

**Example Table: `Product`**
| Column      | Data Type | Notes                        |
|------------|-----------|------------------------------|
| ProductID  | INT       | Unique identifier 🔑         |
| Name       | VARCHAR   | Product name 🏷️             |
| Price      | DECIMAL   | Price in dollars 💵          |
| CreatedAt  | DATETIME  | When product was added 📅     |

---

## 2️⃣ Common Data Types

### 🔹 Varchar (Variable Character)
- Stores **text** of variable length ✏️
- Example: `Name = "Laptop"`

### 🔹 Date and Time
- Stores **dates and timestamps** ⏰
- Example: `CreatedAt = 2025-10-10 14:30:00`

### 🔹 Float and Decimal
- Stores **numbers with decimals** 🔢
- `FLOAT` → approximate values (e.g., 3.14159)
- `DECIMAL` → precise values, ideal for money 💵

### 🔹 Integer Types
- Stores **whole numbers** 🔢
- Example: `Quantity = 10`

### 🔹 Binary Data Types
- Stores **binary data** like images or files 📷📂
- Example: storing a product image as `BLOB`

### 🔹 Character Types
- Stores **fixed-length text** (CHAR) or variable-length (VARCHAR) ✏️
- `CHAR(5)` → always 5 characters
- `VARCHAR(50)` → up to 50 characters

---

## 3️⃣ Advantages of Using Data Types ✅
- **Data Integrity**: Only valid data can be entered 🛡️
- **Efficiency**: Uses storage efficiently 🏋️‍♂️
- **Faster Queries**: Optimized for searching and sorting ⚡
- **Error Prevention**: Reduces mistakes in data entry ❌
- **Consistency**: Ensures all similar data is stored the same way 🔄

---

## 📌 Summary
1. Every **column** in a table has a **data type** 🏷️
2. Common types include `VARCHAR`, `INT`, `DECIMAL`, `DATETIME`, `BLOB` 🧰
3. Proper data types improve **integrity, efficiency, and consistency** in your database 🚀

---

# 🔗 Relational Model Concepts

The **Relational Model** is the foundation of modern databases.

---

## 1️⃣ Sets
- A **set** is a collection of unique elements 🔢
- **Set operations** let you manipulate data sets:
  - **Union ( ∪ )** → combine two sets 🔗
  - **Intersection ( ∩ )** → common elements ✔️
  - **Difference ( − )** → elements in one set but not the other ❌

**Example:**
- Set A = {1, 2, 3}  
- Set B = {2, 3, 4}  
- A ∪ B = {1, 2, 3, 4}  
- A ∩ B = {2, 3}  
- A − B = {1}  

---

## 2️⃣ Relations
- A **relation** is basically a **table** in a database 🗂️
- Each row = **tuple**, each column = **attribute**
- Example Table: `Student`
| StudentID | Name     | Age |
|-----------|----------|-----|
| 1         | Ronnel   | 25  |
| 2         | Maria    | 22  |

---

## 3️⃣ Properties of a Relation
- **Transitivity**: If A → B and B → C, then A → C 🔄  
- **Asymmetry**: If A → B, then B → A **does not hold** ❌

---

## 4️⃣ Components of a Relation
### 🔹 Schema
- Defines the **structure** of a table 🏗️
- Example: `Student(StudentID INT, Name VARCHAR, Age INT)`

### 🔹 Instance
- The **actual data** in the table at a given moment 📝
- Example Table Data:
| StudentID | Name     | Age |
|-----------|----------|-----|
| 1         | Ronnel   | 25  |
| 2         | Maria    | 22  |

---

## 📌 Summary
1. **Sets** → collections of unique items, can perform union, intersection, difference 🔗  
2. **Relations** → tables with rows (tuples) and columns (attributes) 🗂️  
3. **Properties** → transitivity (chain of relationships), asymmetry (direction matters) 🔄  
4. **Components** → schema (table structure) & instance (actual data) 📝  








