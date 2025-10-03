# ============================================================
# 📝 Pandas Exercise: Employee Records
# ============================================================

# 1️⃣ Load the dictionary into a pandas DataFrame
# 2️⃣ Select only the "Name" and "Department" columns
# 3️⃣ Filter all employees from the "IT" department
# 4️⃣ Find the average value of the "Salary" column
# 5️⃣ Sort the dataset by "JoiningDate" (oldest first)
# 6️⃣ Bonus Challenge 🏆
#     • Find which "Employee" has the highest total salary

# Dictionary dataset
import pandas as pd

data = {
    "EmployeeID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Ethan"],
    "Department": ["HR", "IT", "Finance", "IT", "HR"],
    "Salary": [50000, 60000, 55000, 65000, 52000],
    "JoiningDate": ["2020-01-15", "2019-07-23", "2021-03-10", "2018-11-05", "2020-06-17"],
    "City": ["New York", "Chicago", "New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)
print("1.) Loading Dict into DF")
print()
print(df)
print()

name_dept = df[["Name", "Department"]]
print("2.) Name and Department")
print()
print(name_dept)
print()

employee_IT = df[df["Department"] == "IT"]
print("3.) IT Dept Employees")
print()
print(employee_IT)
print()

salaries = df["Salary"].mean()
print("4.) Ave Salary")
print()
print(salaries)
print()

df["JoiningDate"] = pd.to_datetime(df["JoiningDate"])
date_oldest = df.sort_values(by="JoiningDate", ascending=False)
print("5.) Descending Date")
print()
print(date_oldest)
print()

name_salary = df[["Name", "Salary"]]
highest = name_salary.sort_values(
    by="Salary", ascending=False).reset_index(drop=True)
print("6.) BONUS CHALLENGE: Highest Earner Employee")
print()
print(f"Highest Earning Employee: {highest.loc[0, 'Name']}")
print(f"Salary: {highest.loc[0, 'Salary']:,}")

# Saving DF
folder_directory = r"C:\Users\Ronnel\Desktop\IBM Data Engineering\exercises\Python\Python for Data Science, AI, & Devvelopment\Mod_4_Employee Records [pandas]"

df.to_excel(fr"{folder_directory}\hr_new_hires.xlsx", index=False)
