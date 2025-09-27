# ============================================================
# 📊 Exercise: Patient Records Analyzer
# ============================================================
# ✅ Concepts to Practice:
# - open() → Reading a text file
# - pandas → Creating & analyzing a DataFrame
# - class → Wrapping logic inside a class
# - try/except → Handling errors safely
#
# 📝 Task:
# 1. Use open() to read the file "patients.txt".
#    Each line is in this format: Name,Age,Department
#
#    Example file content:
#    John,34,Cardiology
#    Alice,29,Neurology
#    Mark,42,Cardiology
#
# 2. Load the data into a Pandas DataFrame with columns:
#    ["Name", "Age", "Department"]
#
# 3. Build a class `PatientRecords` with:
#    - A method to show average age per department.
#    - A method to find patients older than 40.
#
# 4. Use try/except to handle:
#    - File not found errors
#    - Invalid data format (e.g. missing commas)
#
# ============================================================
import pandas as pd
directory = r"C:\Users\Ronnel\Desktop\IBM Data Engineering\exercises\Python\Python for Data Science, AI, & Devvelopment\Mod_4_Patient Records Analyzer [open, try,  pandas, class]\patients.txt"

try:
    with open(fr"{directory}", "r") as source:
        patients = [line.strip().split(",") for line in source.readlines()]
except FileNotFoundError:
    print("File not Found!")

names, ages, departments = [], [], []

for info in patients:
    names.append(info[0])
    ages.append(int(info[1]))
    departments.append(info[2])
records = {"Name": names,
           "Age": ages,
           "Department": departments
           }
df = pd.DataFrame(records)
#     Name Age  Department
# 0   John  34  Cardiology
# 1  Alice  29   Neurology
# 2   Mark  42  Cardiology


class PatientRecords:

    def __init__(self, dataframe):
        self.df = dataframe

    def ave_age_dept(self):
        return self.df.groupby("Department")["Age"].mean()

    def patients_above_40(self):
        return self.df[self.df["Age"] > 40]


records = PatientRecords(df)

print(records.ave_age_dept())
print(records.patients_above_40())
