# ============================================================
# 📊 Exercise: Hospital Appointments Analyzer
# ============================================================
# ✅ Focus: Pandas
#
# 📝 Task:
# You are given a CSV file "appointments.csv" with the following format:
#
# Patient,Department,Status,WaitTime
# John,Cardiology,Completed,15
# Alice,Neurology,Cancelled,0
# Mark,Cardiology,Completed,25
# Jane,Dermatology,Completed,10
# Bob,Neurology,Completed,30
#
# ============================================================
# ✅ Your Goals:
# ------------------------------------------------------------
# 1. Load the CSV into a Pandas DataFrame.
# 2. Show the first 5 rows.
# 3. Count how many appointments per Department.
# 4. Find the average WaitTime per Department.
# 5. Show only the patients whose appointment was "Completed".
# 6. Sort patients by WaitTime (highest → lowest).
# 7. BONUS: Save the "Completed" appointments into a new CSV file.
# ============================================================

import pandas as pd

directory = r"C:\Users\Ronnel\Desktop\IBM Data Engineering\exercises\Python\Python for Data Science, AI, & Devvelopment\Mod_4_Hospital Appointments Analyzer [open, pandas]"

with open(fr"{directory}\appointments.csv", "r") as file:
    data_raw = []
    for line in file.readlines():
        data_raw.append(line.strip().split(","))

columns = data_raw.pop(0)   # Getting index 0 as columns for df
data = data_raw             # Getting else as data for the columns for df

# Creating elements for columns
patient, dept, status, waittime = [], [], [], []
for info in data:
    patient.append(info[0])
    dept.append(info[1])
    status.append(info[2])
    waittime.append(int(info[3]))

records = {columns[0]: patient,     # Creating a dictionary for df
           columns[1]: dept,
           columns[2]: status,
           columns[3]: waittime}

df = pd.DataFrame(records)          # Creating dataframe
# print(df.head())                    # Printing first 5 rows

#   Patient   Department     Status WaitTime
# 0    John   Cardiology  Completed       15
# 1   Alice    Neurology  Cancelled        0
# 2    Mark   Cardiology  Completed       25
# 3    Jane  Dermatology  Completed       10
# 4     Bob    Neurology  Completed       30

# Counting appointments per dept
appointments_dept = df.groupby("Department")["Patient"].count()
print(appointments_dept)

# Counting ave wait time per dept
ave_waittime_dept = df.groupby("Department")["WaitTime"].mean()
print(ave_waittime_dept)

# Printing completed status only
completed = df[df["Status"] == "Completed"]
print(completed)

# Sorting wait time highest to lowest
waittime_sort = df.sort_values("WaitTime", ascending=False)
print(waittime_sort)

# Saving completed appointments to .csv
completed.to_csv(fr"{directory}\completed.csv", index=False)
