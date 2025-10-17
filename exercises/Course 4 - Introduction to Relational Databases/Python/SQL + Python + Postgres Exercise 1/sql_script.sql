-- Creating Table

-- CREATE TABLE employees_exercise_1(
-- 	id SERIAL PRIMARY KEY,
-- 	name VARCHAR(20),
-- 	department VARCHAR(20),
-- 	salary DECIMAL(10,2)
-- );

-- Inserting Rows

-- INSERT INTO employees_exercise_1 (name, department, salary)
-- VALUES
-- ('Doc', 'Engineering', 42000),
-- ('Nel', 'Engineering', 42000),
-- ('Shed', 'Engineering', 42000),
-- ('Nerb', 'Engineering', 100000),
-- ('Rhea', 'HR', 50000);

-- Adding a column (years_of_service) def val = 1

-- ALTER TABLE employees_exercise_1
-- ADD COLUMN years_of_service INT DEFAULT 1;

-- Updating column (years_of_service)

-- UPDATE employees_exercise_1
-- SET years_of_service = 
-- 	CASE
-- 		WHEN name = 'Doc' THEN 9
-- 		WHEN name = 'Nel' THEN 8
-- 		WHEN name = 'Shed' THEN 9
-- 		WHEN name = 'Nerb' THEN 7
-- 		WHEN name = 'Rhea' THEN 3
-- 		ELSE years_of_service
-- 	END;

-- Dropping years_of_service column

-- ALTER TABLE employees_exercise_1
-- DROP COLUMN years_of_service;

SELECT * FROM employees_exercise_1;