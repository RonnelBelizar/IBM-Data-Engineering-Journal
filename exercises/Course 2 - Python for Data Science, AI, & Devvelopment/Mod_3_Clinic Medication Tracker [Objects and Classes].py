# Exercise: Clinic Medication Tracker
#
# A clinic is treating patients with TB, HIV, and HPV. Each patient has:
# - Name
# - Age
# - Condition
# - Medications (can be "Antibiotic", "Stronger Antibiotic", or empty)
#
# Tasks:
# 1. Create a Patient class with:
#    - __init__ method to set name, age, condition, and medications (default empty list)
#    - is_on_treatment() method → returns True if medications list is not empty
#    - add_medication(med) method → adds a medication to the list
#    - treatment_strength() method → returns:
#         "None" if no medications
#         "Basic" if has "Antibiotic"
#         "Strong" if has "Stronger Antibiotic"
#
# 2. Create 3 patients:
#    - Alice, 32, TB, taking "Antibiotic"
#    - Bob, 45, HIV, taking "Stronger Antibiotic"
#    - Clara, 29, HPV, no medications yet
#
# 3. Print for each patient:
#    - Name
#    - Condition
#    - Whether they are on treatment
#    - Their treatment strength
#
# 4. Add "Stronger Antibiotic" to Clara and print her updated medications list

class Patient:
    # Creating class
    def __init__(self, name, age, condition, medications=None):
        self.name = name
        self.age = age
        self.condition = condition
        self.medications = medications if medications else []

    def is_on_treatment(self):  # Identifying if patient is on medication
        return bool(self.medications)

    def add_medication(self, med):  # Adding medication if there is (default is none)
        self.medications.append(med)

    def treatment_strength(self):   # Treatment strength
        if "Stronger Antibiotic" in self.medications:
            return "Strong"
        elif "Antibiotic" in self.medications:
            return "Basic"
        else:
            return "None"

    def results(self):
        print("---------------" * 3)
        print(f"Name: {self.name}")
        print(f"Condition: {self.condition}")
        print(
            f"Is Patient On Treatment?: {'Yes' if self.is_on_treatment() else 'No'}")
        print(f"Treatment Strength: {self.treatment_strength()}")
        print(f"Medications: {self.medications}")
        print("---------------" * 3)


# Create patients
pt_1 = Patient("Alice", 32, "TB", ["Antibiotic"])
pt_2 = Patient("Bob", 45, "HIV", ["Stronger Antibiotic"])
pt_3 = Patient("Clara", 29, "HPV")

# Adding Medication to Clara
pt_3.add_medication("Antibiotic")

# Print results
pt_1.results()
pt_2.results()
pt_3.results()
