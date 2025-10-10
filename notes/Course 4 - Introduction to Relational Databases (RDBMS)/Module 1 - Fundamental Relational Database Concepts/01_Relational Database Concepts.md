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


