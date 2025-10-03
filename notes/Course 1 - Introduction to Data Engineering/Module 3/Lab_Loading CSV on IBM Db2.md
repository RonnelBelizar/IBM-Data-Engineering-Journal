# Topic: Module 3 - Loading CSV on IBM Db2 Lab

# 🚗 IBM Db2 Data Types Notes (Car Sales Example)

When working with **databases** (like IBM Db2), each column in a table is assigned a **data type**.  
👉 The data type defines **what kind of values** the column can store (numbers, text, dates, etc.).

---

## 📊 Common Db2 Data Types (from your table)

### 🔢 SMALLINT
- **Definition:** A small integer (whole number).  
- **Storage:** 🗄️ 2 bytes.  
- **Range:** ➡️ `-32,768` to `32,767`.  
- **Best for:**  
  - Years (📅 `1995`, `2003`, etc.)  
  - Mileage (if values aren’t too huge)  
  - Small numeric codes  

💡 Think of it as a "budget integer" → saves space when you don’t need big numbers.

---

### ✍️ VARCHAR(n)
- **Definition:** A **variable-length string** (text).  
- **Storage:** 🗄️ Uses only the space the text actually needs + 2 bytes.  
- **Example:** `VARCHAR(18)` → max **18 characters**.  
- **Best for:**  
  - Car Models (`Discovery`, `Freelander`) 🚙  
  - Engine Types (`Diesel`, `Petrol`, `Gas`) ⛽  

💡 Flexible and efficient — doesn’t waste space if the word is short.

---

## 🚘 Your Car Sales Table Example

Here’s the sample data you uploaded to Db2:

| 💰 PRICE | 🚦 MILEAGE | ⛽ ENGTYPE | 📅 YEAR | 🚙 MODEL    |
|----------|------------|------------|---------|-----------  |
| 3300     | 350        | Diesel     | 1995    | Discovery   |
| 3500     | 200        | Petrol     | 2003    | Freelander  |
| 3550     | 255        | Diesel     | 2001    | Discovery   |
| 3700     | 124        | Petrol     | 2005    | Freelander  |
| 3900     | 290        | Diesel     | 1998    | Range Rover |
| 6600     | 298        | Diesel     | 1997    | Discovery   |
| 6900     | 167        | Gas        | 2003    | Freelander  |
| 7000     | 190        | Diesel     | 2004    | Discovery   |
| 7800     | 355        | Diesel     | 2003    | Range Rover |
| 8900     | 295        | Gas        | 2000    | Range Rover |

---

## 🎁 Bonus Notes & Pro Tips

- 🆚 **INTEGER vs SMALLINT**  
  - `INTEGER` = bigger storage, bigger range (`-2 billion to +2 billion`).  
  - Use when numbers can get **really large** (e.g., population, revenue).  
  - `SMALLINT` saves memory if you know values will stay small.  

- 📐 **VARCHAR vs CHAR**  
  - `VARCHAR` = flexible, saves space.  
  - `CHAR(n)` = always takes up the full space (`CHAR(10)` always 10 chars, even if you store "Hi").  
  - Use `CHAR` for fixed-length stuff (postal codes, country codes).  

- 📦 **Why care about data types?**  
  - 💾 Saves storage.  
  - ⚡ Improves query performance.  
  - ✅ Prevents invalid data (e.g., you can’t put text inside a SMALLINT).  

---

✨ TL;DR:  
- `SMALLINT` → small whole numbers.  
- `VARCHAR(n)` → flexible text storage.  
- Pick wisely to balance **performance + storage + accuracy**.


