-- Creating a new column for new_salary

-- ALTER TABLE employees_exercise_1
-- ADD COLUMN new_salary NUMERIC(10,2);

-- Giving a 10% increase on salaries

-- UPDATE employees_exercise_1
-- SET new_salary = salary + salary*0.1;

-- Creating a new column for bonus_eligible

-- ALTER TABLE employees_exercise_1
-- ADD COLUMN bonus_eligible BOOL DEFAULT FALSE;

-- Updating values for column bonus_eligible

UPDATE employees_exercise_1
SET bonus_eligible =
	CASE
		WHEN salary > 50000 THEN TRUE
		ELSE FALSE
	END;

SELECT * FROM employees_exercise_1;