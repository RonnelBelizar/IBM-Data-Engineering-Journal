# Topic: Module 4 - Working With Data in Python

# Topic: Module 4 - Python Programming Fundamentals pt. 3

# 📖 Reading Files with Python

---

## 🔑 Why Read Files in Python?

    • Programs often need to work with data stored in files (e.g., .txt, .csv).  
    • Python provides simple built-in functions to open, read, and manage files.  
    • Common tasks: open a file, check its mode, read contents, then close it.  

---

## 🛠️ The `open()` Function

    • Syntax: open(filename, mode)  
    • filename → name of the file you want to access.  
    • mode → specifies how you want to open the file (read, write, append, etc.).  

    Example:
        file = open("example.txt", "r")

        • "example.txt" → file name.  
        • "r" → mode (read mode).  
        • file → variable that now represents the opened file.  

---

## 📝 File Name Attribute (`name`)

    • You can check which file has been opened with .name.  

    Example:
        file = open("example.txt", "r")
        print(file.name)

        Output:
        example.txt

---

## ⚙️ File Mode Attribute (`mode`)

    • You can check the mode in which the file was opened using .mode.  

    Example:
        file = open("example.txt", "r")
        print(file.mode)

        Output:
        r

## 1. Common Modes
    • "r" → Read (default).  
        - Opens file for reading only.  
        - ❌ Error if file doesn’t exist.  
        - Cursor starts at beginning.  
        ✅ Example:

            with open("file.txt", "r") as f:
                print(f.read())

    • "w" → Write.  
        - Opens file for writing.  
        - ⚠️ Overwrites file if it exists.  
        - Creates new file if it doesn’t exist.  
        ✅ Example:

            with open("file.txt", "w") as f:
                f.write("This replaces all content!")

    • "a" → Append.  
        - Opens file for writing at the end.  
        - Does NOT erase existing content.  
        - Creates new file if it doesn’t exist.  
        ✅ Example:

            with open("file.txt", "a") as f:
                f.write("\nThis gets added to the end.")

    • "rb" → Read in Binary Mode.  
        - Reads file in binary (not text).  
        - Use for images, videos, PDFs.  
        ✅ Example:

            with open("image.jpg", "rb") as f:
                data = f.read()

    • "wb" → Write in Binary Mode.  
        - Writes in binary.  
        - Use when saving images, videos, etc.  
        ✅ Example:
        
            with open("copy.jpg", "wb") as f:
                f.write(data)

---

## 2. Combined Modes

    • "w+" → Write + Read.  
        - File is truncated (emptied) first.  
        - Creates new file if it doesn’t exist.  
        ✅ Example:

            with open("file.txt", "w+") as f:
                f.write("Hello!")
                f.seek(0)   # rewind cursor
                print(f.read())  # prints "Hello!"

    • "r+" → Read + Write.  
        - Does NOT truncate file.  
        - File must already exist.  
        ✅ Example:

            with open("file.txt", "r+") as f:
                content = f.read()
                f.seek(0)
                f.write("New ")
                f.write(content)

    • "a+" → Append + Read.  
        - Opens file for reading & appending.  
        - Cursor starts at END of file (need seek(0) to read from start).  
        ✅ Example:

            with open("file.txt", "a+") as f:
                f.write("\nAdded line")
                f.seek(0)  # go back to start
                print(f.read())

---

## ❌ Closing Files (`close()`)

    • Always close a file when done to free up resources.  
    • If not closed, it may lead to memory issues or data corruption.  

    Example:
        file = open("example.txt", "r")
        content = file.read()
        print(content)
        file.close()

---

## ✅ Using `with` (Best Practice)

    • The `with` statement ensures the file is closed automatically.  
    • Even if an error occurs, Python will safely close the file.  

    Example:
        with open("example.txt", "r") as file:
            content = file.read()
            print(content)

        • No need to call close() → handled automatically.  

---

## 🧩 Reading Files Line by Line

    • Useful for large files when you don’t want to read everything at once.  

    Example:
        with open("example.txt", "r") as file:
            for line in file:
                print(line.strip())

        • for line in file → loops through each line.  
        • line.strip() → removes extra spaces or newline characters (\n).  

---

## ✨ Key Points

    • Use open("filename", "mode") to open files.  
    • Always close files with close(), or better, use with.  
    • .name → returns the filename.  
    • .mode → returns the file mode.  
    • Common modes: "r", "w", "a", "rb", "wb".  
    • ✅ Best practice: use with open(...) for safe file handling.  

---



