-- # 🧑‍💼 Employee & Department Database Exercise

-- ## Objective
-- Practice creating relational tables, foreign keys, cascading actions, and joins.

-- ---

-- ## Instructions

-- 1️⃣ **Create a database** called `company_practice_db`.

-- 2️⃣ **Create a table `departments`** with:
-- - `dept_id` (INT, PRIMARY KEY)
-- - `dept_name` (VARCHAR, required)
-- - Optional: `location` (VARCHAR)

-- 3️⃣ **Create a table `employees`** with:
-- - `emp_id` (INT, PRIMARY KEY or SERIAL)
-- - `dept_id` (INT, foreign key referencing `departments`)
-- - `emp_name` (VARCHAR, required)
-- - `position` (VARCHAR, required)
-- - `salary` (NUMERIC, must be > 0)
-- - **Set foreign key actions**:
--   - `ON UPDATE CASCADE`
--   - `ON DELETE CASCADE`

-- 4️⃣ **Insert sample data**:
-- - At least 3 departments (e.g., Engineering, IT, HR)
-- - At least 4 employees assigned to these departments

-- 5️⃣ **Create a table `projects`** with:
-- - `project_id` (INT, PRIMARY KEY)
-- - `project_name` (VARCHAR, required)
-- - `emp_id` (INT, foreign key referencing `employees`)
-- - `start_date` (DATE)
-- - `end_date` (DATE)
-- - Foreign key with `ON DELETE CASCADE`

-- 6️⃣ **Insert at least 2 projects** assigned to employees.

-- 7️⃣ **Practice queries**:
-- - Show all employees with their department names
-- - Show all projects with employee and department names

-- 8️⃣ **Test cascading behavior**:
-- - Delete a department and observe what happens to its employees and projects
-- - Update a department's `dept_id` and see how it affects employees


CREATE TABLE departments(
	dept_id INT PRIMARY KEY,
	dept_name VARCHAR (20) NOT NULL,
	location VARCHAR (20)
);

CREATE TABLE employees(
	emp_id SERIAL,
	dept_id INT,
	emp_name VARCHAR(25) NOT NULL,
	position VARCHAR (25) NOT NULL,
	salary NUMERIC(10, 2) CHECK (salary>0),
	PRIMARY KEY (emp_id),
	FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

INSERT INTO departments(dept_id, dept_name)
	VALUES
		(1, 'Engineering'),
		(2, 'HR'),
		(3, 'IT');

INSERT INTO employees(dept_id, emp_name, position, salary)
	VALUES
		(1, 'Ronnel', 'Senior FSE', 75000),
		(2, 'Rhea', 'Admin', 150000),
		(3, 'Lara', 'Admin', 250000);

CREATE TABLE projects(
	project_id INT,
	project_name VARCHAR(25) NOT NULL,
	emp_id INT,
	start_date DATE,
	end_date DATE,
	FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
		ON DELETE CASCADE
);

INSERT INTO projects(project_id, project_name, emp_id, start_date, end_date)
	VALUES
		(100, 'Notary of Documents', 2, '2025/10/25', NULL),
		(200, 'Installation of CCTV', 3, '2025/10/10', NULL);

SELECT * FROM projects;

