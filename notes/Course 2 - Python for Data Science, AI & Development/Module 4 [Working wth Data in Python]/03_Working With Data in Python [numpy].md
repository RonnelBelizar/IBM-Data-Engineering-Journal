# Topic: Module 4 — Working With Data in Python

# 📘 Module: NumPy Essentials  

---

## 🔎 Definition & Importance  

    • 📖 Definition → NumPy (Numerical Python) is a **Python library** used for handling **large arrays, matrices, and numerical computations** efficiently.  

    • 🚀 Importance →  
        - Powers Data Engineering, Data Science, ML & AI.  
        - Provides **fast vectorized operations** (no slow loops).  
        - Integrates well with other libraries (Pandas, SciPy, TensorFlow, etc.).  
        - Backbone for **data analysis, image processing, simulations, and statistics**.  

---

## 📏 1D NumPy Arrays  

    import numpy as np  

    arr = np.array([1, 2, 3, 4, 5])     # 1D Array  

    print(arr)  

🧾 Output → [1 2 3 4 5]  
🎯 Think of it as a simple row of numbers → like a **vector** in math.  

---

## 🔤 Basics and Array Creation  

    # Different ways to create arrays  

    a = np.array([1, 2, 3])             # From list  
    b = np.zeros(5)                     # Array of zeros  
    c = np.ones(5)                      # Array of ones  
    d = np.arange(1, 10, 2)             # Range with step  
    e = np.linspace(0, 1, 5)            # Evenly spaced numbers  

    print(a, b, c, d, e)  

---

## 🎯 Indexing and Slicing  

    arr = np.array([10, 20, 30, 40, 50])  

    print(arr[0])       # First element → 10  
    print(arr[-1])      # Last element → 50  
    print(arr[1:4])     # Slice → [20 30 40]  

📌 Same concept as Python lists but **faster & optimized**.  

---

## ➕ Basic Operations  

✨ Vector Add & Subtract  

    x = np.array([1, 2, 3])  
    y = np.array([4, 5, 6])  

    print(x + y)        # [5 7 9]  
    print(y - x)        # [3 3 3]  

✖️ Array Multiplication with a Scalar  

    arr = np.array([1, 2, 3, 4])  

    print(arr * 10)     # [10 20 30 40]  

🔄 Product of Two NumPy Arrays  

    a = np.array([1, 2, 3])  
    b = np.array([4, 5, 6])  

    print(a * b)        # Element-wise product → [4 10 18]  

📌 This is **Hadamard product** (not matrix multiplication).  

---

## 🌐 Universal Functions (ufuncs)  

    arr = np.array([0, np.pi/2, np.pi])  

    print(np.sin(arr))        # [0. 1. 0.]  
    print(np.exp(arr))        # [ 1.     4.81   23.14]  
    print(np.sqrt([1,4,9]))   # [1. 2. 3.]  

✅ ufuncs → Apply **fast math** to entire arrays without looping.  

---

## 📊 Plotting Mathematical Functions with Matplotlib  

    import matplotlib.pyplot as plt  

    x = np.linspace(-10, 10, 100)  
    y = np.sin(x)  

    plt.plot(x, y, label="sin(x)")  
    plt.xlabel("x-axis")  
    plt.ylabel("y-axis")  
    plt.title("📉 Plot of Sine Function")  
    plt.legend()  
    plt.show()  

---

## 🖼️ Graphical Representation of NumPy Concepts  

          +---------------------------+  
          |         NumPy             |  
          +---------------------------+  
                    |  
                    v  
          +---------------------------+  
          |      Array Object         |  
          |   (1D, 2D, ND Arrays)     |  
          +---------------------------+  
                    |  
                    v  
          +---------------------------+  
          |  Fast Math Operations     |  
          |  (Vectorized, ufuncs)     |  
          +---------------------------+  
                    |  
                    v  
          +---------------------------+  
          | Visualization (Matplotlib)|  
          +---------------------------+  

---

# 📘 2D NumPy Arrays  

---

## 🔎 What are 2D Arrays?  

    • 📖 Definition → A **2D NumPy array** is like a **table (rows & columns)** or a **matrix** in mathematics.  
    • 🏗️ Structure → Arranged in rows and columns → `shape = (rows, columns)`  
    • 💡 Use Cases → Representing datasets, images (pixels), matrices for linear algebra, etc.  

---

## 🛠️ Creating 2D Arrays  

    import numpy as np  

    # Manual 2D array  
    arr = np.array([[1, 2, 3],  
                    [4, 5, 6],  
                    [7, 8, 9]])  

    print(arr)  

🧾 Output →  
    [[1 2 3]  
     [4 5 6]  
     [7 8 9]]  

---

## 📐 Shape and Dimensions  

    print(arr.shape)     # (3, 3) → 3 rows, 3 columns  
    print(arr.ndim)      # 2 → 2 dimensions  
    print(arr.size)      # 9 → total elements  

---

## 🎯 Indexing in 2D Arrays  

    print(arr[0, 0])     # Element at row 0, col 0 → 1  
    print(arr[1, 2])     # Element at row 1, col 2 → 6  
    print(arr[-1, -1])   # Last element → 9  

---

## ✂️ Slicing in 2D Arrays  

    print(arr[0:2, 1:3])     # Submatrix → rows 0–1, cols 1–2  

🧾 Output →  
    [[2 3]  
     [5 6]]  

---

## 🔄 Basic Operations on 2D Arrays  

✨ Vectorized Addition  

    a = np.array([[1, 2],  
                  [3, 4]])  

    b = np.array([[5, 6],  
                  [7, 8]])  

    print(a + b)  

🧾 Output →  
    [[ 6  8]  
     [10 12]]  

✖️ Scalar Multiplication  

    print(a * 10)  

🧾 Output →  
    [[10 20]  
     [30 40]]  

---

## 📊 Matrix Multiplication  

    # Using @ operator  
    print(a @ b)  

    # Or with np.dot()  
    print(np.dot(a, b))  

🧾 Output →  
    [[19 22]  
     [43 50]]  

📌 This is **true matrix multiplication**, not element-wise.  

---

## 🌐 Universal Functions on 2D Arrays  

    c = np.array([[1, 4, 9],  
                  [16, 25, 36]])  

    print(np.sqrt(c))    # Square root of all elements  
    print(np.exp(c))     # Exponential of all elements  

---

## 🖼️ Graphical Representation of 2D Array (3x3 Example)  

          C0   C1   C2  
        +----+----+----+  
    R0  |  1 |  2 |  3 |  
        +----+----+----+  
    R1  |  4 |  5 |  6 |  
        +----+----+----+  
    R2  |  7 |  8 |  9 |  
        +----+----+----+  

📌 Each element is accessed as → arr[row, column]  

---

