-- 🏥 HEALTHCARE DATABASE EXERCISE

-- 1️⃣ Create a new database named `healthcare_db`
--    and switch to it.

-- 2️⃣ Create the following tables:

-- a. patients
--    - patient_id (INT, Primary Key)
--    - first_name (VARCHAR)
--    - last_name (VARCHAR)
--    - birth_date (DATE)
--    - gender (CHAR)
--    - contact_number (VARCHAR)

-- b. doctors
--    - doctor_id (INT, Primary Key)
--    - first_name (VARCHAR)
--    - last_name (VARCHAR)
--    - specialization (VARCHAR)

-- c. appointments
--    - appointment_id (INT, Primary Key)
--    - patient_id (INT, Foreign Key → patients.patient_id)
--    - doctor_id (INT, Foreign Key → doctors.doctor_id)
--    - appointment_date (DATE)
--    - diagnosis (VARCHAR)
--    - treatment (VARCHAR)

-- 3️⃣ Insert at least 5 patients, 3 doctors, and 5 appointments.

-- 4️⃣ Write queries to:
--    a. View all appointments with the patient's and doctor’s full names.
--    b. Find all appointments handled by a specific doctor (e.g., “Dr. Smith”).
--    c. List all patients born before 1990.
--    d. Show the number of appointments each doctor has.
--    e. Display all appointments in order of appointment_date (latest first).
--    f. Find patients who have more than one appointment.

-- 5️⃣ BONUS:
--    Create a view called `appointment_summary`
--    that shows patient_name, doctor_name, specialization, and appointment_date.



CREATE DATABASE healthcare_db;
USE healthcare_db;

CREATE TABLE patients(
	patient_id INT PRIMARY KEY,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    birthdate DATE,
    gender CHAR(1) NOT NULL,
    contact_number VARCHAR(15)
);

CREATE TABLE doctors(
	doctor_id INT PRIMARY KEY,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    specialization VARCHAR(20)
);

CREATE TABLE appointments(
	appointments_id INT PRIMARY KEY,
    patient_id INT,
    doctor_id INT,
    appointment_date DATE,
    diagnosis VARCHAR(20) NOT NULL,
    treatment VARCHAR(20),
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
);

INSERT INTO patients(patient_id, first_name, last_name, birthdate, gender, contact_number)
VALUES
	(1, 'Ronnel', 'Belizar', '1996-01-16', 'M', '+639154797401'),
    (2, 'John Monsour', 'Doctor', '1995-05-05', 'M', '+639154125125'),
    (3, 'Shed', 'Daroya', '1989-10-27', 'M', '+639274568974'),
    (4, 'Nerb', 'Bagbaguen', '1995-12-25', 'M', '+639178521234'),
    (5, 'Rhea', 'Canelas', '1999-11-01', 'F', '+639153578521');

INSERT INTO doctors(doctor_id, first_name, last_name, specialization)
VALUES
	(1, 'Lara', 'Dacayo', 'HIV Specialist'),
    (2, 'Mike', 'Pritus', 'CT_NG Specialist'),
    (3, 'Harold', 'Toco', 'General Practitioner');

INSERT INTO appointments(appointments_id, patient_id, doctor_id, appointment_date, diagnosis, treatment)
VALUES
	(1, 2, 1, '2025-10-25', 'HIV', 'Avoid Laica'),
    (2, 5, 3, '2025-10-19', 'Patrickolosis', 'Resign'),
    (3, 3, 2, '2025-10-21', 'Boredom', 'Study Python');

--    a. View all appointments with the patient's and doctor’s full names.

SELECT
	appointments.appointments_id,
	CONCAT(patients.first_name, ' ', patients.last_name) AS patient_name,
    CONCAT(doctors.first_name, ' ', doctors.last_name) AS doctor_name,
    appointments.diagnosis
FROM appointments
JOIN patients
	ON appointments.patient_id = patients.patient_id
JOIN doctors
	ON appointments.doctor_id = doctors.doctor_id;

--    b. Find all appointments handled by a specific doctor (e.g., “Dr. Smith”).

SELECT appointments_id, CONCAT(d.first_name, ' ', d.last_name) as doctor_name, appointment_date
FROM appointments a
JOIN doctors d
ON a.doctor_id = d.doctor_id
WHERE a.doctor_id = 3;

--    c. List all patients born before 1990.

SELECT 
	CONCAT(first_name, ' ', last_name) AS patient_name_born_before_1990
FROM patients
WHERE birthdate < '1990-01-01';

--    d. Show the number of appointments each doctor has.

SELECT
	CONCAT(d.first_name, ' ', d.last_name) AS doctor_name,
    COUNT(a.doctor_id) AS number_of_appointments
FROM doctors d
JOIN appointments a
	ON d.doctor_id = a.doctor_id
GROUP BY d.doctor_id;

--    e. Display all appointments in order of appointment_date (latest first).

SELECT *
FROM appointments
ORDER BY appointment_date DESC;

--    f. Find patients who have more than one appointment.

SELECT
	CONCAT(p.first_name, ' ', p.last_name) AS patient_name,
    COUNT(a.appointments_id) AS number_of_appointments
FROM patients p
JOIN appointments a
	ON p.patient_id = a.patient_id
GROUP BY p.patient_id
HAVING COUNT(a.appointments_id) > 1;

--    Create a view called `appointment_summary`
--    that shows patient_name, doctor_name, specialization, and appointment_date.

CREATE VIEW appointment_summary AS
	SELECT
		CONCAT(p.first_name, ' ', p.last_name) AS patient_name,
        CONCAT(d.first_name, ' ', d.last_name) AS doctor_name,
        d.specialization,
        a.appointment_date
    FROM appointments a
    JOIN patients p
		ON a.patient_id = p.patient_id
    JOIN doctors d
		ON a.doctor_id = d.doctor_id;

SELECT * FROM appointment_summary;

```markdown    
# 🏥 SQL Cheatsheet — Healthcare Database

| #  | SQL Concept / Query | Short Definition                            | Example / Snippet                                             |
|----|---------------------|---------------------------------------------|---------------------------------------------------------------|
| 1  | CREATE DATABASE     | Creates a new database                      | CREATE DATABASE healthcare_db;                                |
| 2  | USE                 | Switches to a specific database             | USE healthcare_db;                                            |
| 3  | CREATE TABLE        | Defines a new table and its columns         | CREATE TABLE patients (...);                                  |
| 4  | PRIMARY KEY         | Uniquely identifies each record in a table  | patient_id INT PRIMARY KEY                                    |
| 5  | FOREIGN KEY         | Connects tables using related columns       | FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)         |
| 6  | INSERT INTO         | Adds new data (rows) into a table           | INSERT INTO patients VALUES (...);                            |
| 7  | SELECT              | Retrieves data from one or more tables      | SELECT * FROM patients;                                       |
| 8  | JOIN                | Combines rows from related tables           | SELECT * FROM patients JOIN appointments ON ...;              |
| 9  | CONCAT()            | Joins text values (e.g., first + last name) | CONCAT(first_name, ' ', last_name)                            |
| 10 | WHERE               | Filters rows based on a condition           | WHERE birthdate < '1990-01-01'                                |
| 11 | GROUP BY            | Groups rows that share a column value       | GROUP BY doctor_id                                            |
| 12 | HAVING              | Filters grouped results (after GROUP BY)    | HAVING COUNT(*) > 1                                           |
| 13 | COUNT()             | Counts number of rows or items              | COUNT(appointment_id)                                         |
| 14 | ORDER BY            | Sorts results ascending/descending          | ORDER BY appointment_date DESC                                |
| 15 | CREATE VIEW         | Saves a query as a reusable virtual table   | CREATE VIEW appointment_summary AS ...                        |


**Tip Summary**
- JOIN → Combine tables  
- GROUP BY → Summarize data  
- HAVING → Filter grouped data  
- ORDER BY → Sort results  
- VIEW → Store complex queries for reuse  
```
    
    


