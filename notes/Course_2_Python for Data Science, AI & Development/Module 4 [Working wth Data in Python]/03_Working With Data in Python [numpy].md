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
