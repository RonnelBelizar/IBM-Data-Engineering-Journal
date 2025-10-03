# Topic: Module 4 - Working with Data in Python

# 📊 Pandas: Loading Data

---

## 🔎 What is Pandas?
🐼 Pandas is a **Python library** for data manipulation & analysis.  

- 📍 Core Structures:  
  • **Series** → 1D labeled array (like a single column in Excel).  
  • **DataFrame** → 2D labeled table (like an Excel sheet or SQL table).  

👉 Makes working with **structured/tabular data** super easy.  

---

## 🛠️ Importing Pandas
📌 Standard alias when importing:
```python
import pandas as pd
```

---

## 📥 Loading Data

### 🗂️ a) From CSV
```python
df = pd.read_csv("students.csv")
```

📄 Example `students.csv` file:

| 🧑 Name   | 🎂 Age | 🏅 Grade |
|-----------|--------|----------|
| Alice     | 20     | A        |
| Bob       | 21     | B        |
| Charlie   | 19     | A        |

---

### 📊 b) From Excel
```python
df = pd.read_excel("students.xlsx")
```
⚠️ Requires the **`openpyxl`** package installed.  

---

### 🧾 c) From Dictionaries
```python
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [20, 21, 19],
    "Grade": ["A", "B", "A"]
}
df = pd.DataFrame(data)
```

🗂️ Output DataFrame:

| 🧑 Name   | 🎂 Age | 🏅 Grade |
|-----------|--------|----------|
| Alice     | 20     | A        |
| Bob       | 21     | B        |
| Charlie   | 19     | A        |

---

## 🧑‍💻 Using DataFrames

### 👀 Viewing Data
```python
df.head()   # Shows first 5 rows
df.tail()   # Shows last 5 rows
```

---

### 📌 Selecting Columns
```python
df["Name"]              # Single column
df[["Name", "Grade"]]   # Multiple columns
```

---

### 🔢 Access by Position → `iloc`
```python
df.iloc[0, 0]       # Row 0, Column 0 → "Alice"
df.iloc[0:2, 0:2]   # First 2 rows, first 2 columns
```

---

### 🏷️ Access by Label → `loc`
```python
df.loc[0, "Name"]   # Row 0, Column "Name" → "Alice"
```

---

### ✍️ Change Index Labels
```python
df_new = df.copy()
df_new.index = ['a', 'b', 'c']
```

🆕 Output:

| 🔑 Index | 🧑 Name   | 🎂 Age | 🏅 Grade |
|----------|-----------|--------|----------|
| a        | Alice     | 20     | A        |
| b        | Bob       | 21     | B        |
| c        | Charlie   | 19     | A        |

---

## 📝 Summary
✨ Pandas helps load & manipulate structured data.  
✅ Load from **CSV, Excel, or Dictionaries**.  
✅ DataFrame = table-like structure (like SQL/Excel).  
✅ Use `.head()`, `.iloc[]`, `.loc[]` to explore & access.  
✅ Index labels can be customized for readability.  

🚀 With Pandas, you handle data **faster, cleaner, smarter**!

---

# 📊 Pandas: Working with and Saving Data

---

## 🔎 Listing Unique Values
Sometimes you want to find **all distinct values** in a column.

```python
import pandas as pd

# Sample DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "Alice", "Bob"],
    "Age": [20, 21, 19, 20, 21],
    "Grade": ["A", "B", "A", "A", "B"]
}
df = pd.DataFrame(data)

# 🎯 Get unique values from "Name"
print(df["Name"].unique())

# 🎯 Get number of unique values
print(df["Name"].nunique())
```

📌 Output:
```
['Alice' 'Bob' 'Charlie']
3
```

---

## 🏗️ Creating a Database (Filtering Data)

### ➕ Applying Conditions / Inequalities
You can filter rows using operators like `==`, `!=`, `>`, `<`, `>=`, `<=`.

```python
# 🎯 Students older than 19
older_students = df[df["Age"] > 19]
print(older_students)

# 🎯 Students with Grade A
grade_a = df[df["Grade"] == "A"]
print(grade_a)
```

📌 Original Table:

| 🧑 Name   | 🎂 Age | 🏅 Grade |
|-----------|--------|----------|
| Alice     | 20     | A        |
| Bob       | 21     | B        |
| Charlie   | 19     | A        |
| Alice     | 20     | A        |
| Bob       | 21     | B        |

📌 Filtered (Age > 19):

| 🧑 Name   | 🎂 Age | 🏅 Grade |
|-----------|--------|----------|
| Alice     | 20     | A        |
| Bob       | 21     | B        |
| Alice     | 20     | A        |
| Bob       | 21     | B        |

---

## 💾 Saving Data

Pandas allows exporting to many formats. Most common: **CSV & Excel**.

```python
# Save DataFrame to CSV
df.to_csv("students_cleaned.csv", index=False)

# Save DataFrame to Excel
df.to_excel("students_cleaned.xlsx", index=False)
```

📌 Notes:
- `index=False` → prevents pandas from writing row numbers as a column.  
- You can specify file path, e.g., `r"C:\Users\Ronnel\Desktop\students.csv"`.  

---

## 📝 Summary
✨ Key skills for working with DataFrames:
- 🔍 `unique()` → list distinct values.  
- 🔢 `nunique()` → count unique values.  
- ⚖️ Apply **filters/inequalities** to create subsets.  
- 💾 Save data into **CSV/Excel** for sharing & later use.  

🚀 This turns your DataFrame into a mini **database** you can query & export!

---



