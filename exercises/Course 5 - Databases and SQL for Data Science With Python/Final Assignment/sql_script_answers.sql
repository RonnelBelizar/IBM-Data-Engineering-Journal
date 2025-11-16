-- #1
DESCRIBE chicago_crime_data;
SELECT COUNT(case_number) FROM chicago_crime_data;

-- 533

-- #2
DESCRIBE census_data;
SELECT community_area_name, community_area_number
FROM census_data
WHERE per_capita_income < 11000;

-- West Garfield Park	26
-- South Lawndale	30
-- Fuller Park	37
-- Riverdale	54

-- #3
DESCRIBE chicago_crime_data;
SELECT * FROM chicago_crime_data LIMIT 10;

-- Cannot answer the question: the dataset does not contain age or minor-related information.

-- #4
DESCRIBE chicago_crime_data;
SELECT * FROM chicago_crime_data WHERE description LIKE '%CHILD%';
SELECT description FROM chicago_crime_data WHERE description LIKE '%CHILD%';

SELECT * FROM chicago_crime_data WHERE primary_type = 'KIDNAPPING' AND description LIKE '%CHILD%';

-- 0

-- #5
DESCRIBE chicago_crime_data;
SELECT DISTINCT(location_description) FROM chicago_crime_data WHERE location_description LIKE '%SCHOOL%';
SELECT DISTINCT(primary_type) FROM chicago_crime_data WHERE location_description LIKE '%SCHOOL%';

-- BATTERY
-- CRIMINAL DAMAGE
-- NARCOTICS
-- ASSAULT
-- CRIMINAL TRESPASS
-- PUBLIC PEACE VIOLATION

-- #6
DESCRIBE chicago_public_schools;
SELECT * FROM chicago_public_schools LIMIT 10;
SELECT `elementary,_middle,_or_high_school`, AVG(safety_score) as avg_safety_score
FROM chicago_public_schools
GROUP BY (`elementary,_middle,_or_high_school`);

-- ES	49.52038369304557
-- HS	49.62352941176471
-- MS	48

-- #7
SELECT * FROM census_data LIMIT 10;
SELECT community_area_name, percent_households_below_poverty FROM census_data
ORDER BY percent_households_below_poverty DESC
LIMIT 5;

-- Riverdale	56.5
-- Fuller Park	51.2
-- Englewood	46.6
-- North Lawndale	43.1
-- East Garfield Park	42.4

-- #8
SELECT * FROM chicago_crime_data LIMIT 10;
SELECT community_area_number, COUNT(case_number) AS count FROM chicago_crime_data
GROUP BY community_area_number
ORDER BY COUNT(case_number) DESC;

-- 25

-- #9
SELECT * FROM census_data LIMIT 10;
SELECT community_area_name FROM census_data
WHERE hardship_index = (SELECT MAX(hardship_index) FROM census_data);

-- Riverdale

-- #10
SELECT * FROM chicago_crime_data LIMIT 10;
SELECT * FROM census_data LIMIT 10;
SELECT 
	cd.community_area_name,  COUNT(ccd.case_number) AS count
FROM
	census_data cd
JOIN 
	chicago_crime_data ccd
	ON 
		cd.community_area_number = ccd.community_area_number
GROUP BY 
	cd.community_area_name
ORDER BY 
	count DESC
LIMIT 1;

-- Austin	43