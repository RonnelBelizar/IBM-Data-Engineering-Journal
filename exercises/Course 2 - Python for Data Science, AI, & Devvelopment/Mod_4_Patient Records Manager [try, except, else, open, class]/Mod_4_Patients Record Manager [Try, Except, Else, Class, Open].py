# 🩺 Practice Problem: Patient Records Manager
# ============================================================
# 📌 Problem Description:
# You are tasked with creating a simple Patient Records Manager program in Python.
# ============================================================
# ✅ Requirements
# ============================================================
# 1. Class & Function
#    - Create a class called Patient.
#    - The class should have attributes like name, age, and diagnosis.
#    - Add a method summary() that returns a formatted string with the patient’s details.

# 2. File Handling (open)
#    - Read patient data from a file called "patients.txt".
#    - Each line in the file is formatted like this:
#          Name,Age,Diagnosis
#      Example:
#          John Doe,45,Diabetes
#          Maria Cruz,30,Hypertension

# 3. Error Handling (try, except, else)
#    - Use try/except to handle:
#        * File not found errors.
#        * Invalid age values (non-numeric).
#    - If no exception occurs, use else to display all patient summaries.

# 4. Challenge ⚡
#    - If a patient is over 60 years old, print a special warning:
#          ⚠️ High-risk patient: <Name>

class Patient:  # Creating Class
    def __init__(self, name, age, diagnosis):   # Creating Attributes
        self.name = name
        self.age = age
        self.diagnosis = diagnosis

    def summary(self):  # Creating Method — Display
        print(f"Patient Name: {self.name.title()}")
        print(f"Patient Age: {self.age}")
        print(f"Diagnosis: {self.diagnosis}")
        if self.age > 60:
            print("High Risk: Age above 60!")
        print("-"*20)


patients_directory = r"C:\Users\Ronnel\Desktop\IBM Data Engineering\exercises\Python\Python for Data Science, AI, & Devvelopment\Mod_4_Patient Records Manager [try, except, else, open, class]"
text_file = "patients.txt"
patient_info = []
try:
    with open(fr"{patients_directory}\{text_file}", "r") as source:
        info = source.readlines()
        for line in info:
            seggregate = line.strip().split(",")
            name = seggregate[0]
            age = seggregate[1]
            diagnosis = seggregate[2]
            try:    # Trying if age is digit
                age = int(age)
            except ValueError:
                print(f"Patient \"{name}\" Download Unsuccessful")
                print(f"Patient age ({age}) is not a digit.")
                print("-"*50)
                continue
            else:   # Appending objects in a list if Age is a digit
                patient = Patient(name, age, diagnosis)
                patient_info.append(patient)
                print(f"Patient \"{name}\" Download Successful")
                print("-"*50)
except FileNotFoundError:
    print(f"\"{text_file}\" Not Found")
for patient in patient_info:
    patient.summary()
