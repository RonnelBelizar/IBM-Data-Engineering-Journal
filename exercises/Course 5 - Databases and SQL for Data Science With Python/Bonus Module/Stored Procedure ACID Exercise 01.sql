-- # Stored Procedure Exercise – Library System

-- ## Scenario
-- You manage a library database.  
-- Create a stored procedure to automate **lending books** to members.

-- ## Tables

-- ### books
-- | Column  | Type         |
-- |---------|--------------|
-- | book_id | INT (PK)     |
-- | title   | VARCHAR(100) |
-- | author  | VARCHAR(50)  |
-- | copies  | INT          |

-- ### members
-- | Column    | Type        |
-- |-----------|------------|
-- | member_id | INT (PK)   |
-- | name      | VARCHAR(50)|
-- | join_date | DATE       |

-- ### loans
-- | Column      | Type                |
-- |------------|--------------------|
-- | loan_id    | INT (PK, AI)       |
-- | book_id    | INT (FK → books)   |
-- | member_id  | INT (FK → members) |
-- | loan_date  | DATE               |
-- | return_date| DATE               |

-- ## Task
-- Create a stored procedure **`LendBook`**:

-- ### Inputs
-- - `p_book_id INT`  
-- - `p_member_id INT`  
-- - `p_loan_date DATE`  

-- ### Logic
-- 1. Check if **book exists**.  
-- 2. Check if **member exists**.  
-- 3. Check if **book has ≥1 copy**.  
-- 4. If valid:  
--    - Insert into `loans`.  
--    - Decrease `books.copies` by 1.  
-- 5. If invalid → throw error.

-- ## Bonus
-- Add an **OUT parameter** to return the new `loan_id`.

-- **Practice Focus:**  
-- - Foreign key relationships  
-- - Validation  
-- - Updating another table  
-- - Optional: Transactions


DELIMITER //

CREATE PROCEDURE LendBook(
	IN p_book_id INT,
    IN p_member_id INT,
    IN p_loan_date DATE)
BEGIN
	DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
		ROLLBACK;
        SIGNAL SQLSTATE '45000'
			SET MESSAGE_TEXT = 'Error Occured';
	END;
    
    START TRANSACTION;
		IF p_book_id IN (SELECT book_id FROM books WHERE copies >= 1) AND
			p_member_id IN (SELECT member_id FROM members)            
            THEN
				INSERT INTO loans(book_id, member_id, loan_date)
					VALUES(
						p_book_id,
						p_member_id,
						p_loan_date);
				UPDATE books SET copies = copies-1 WHERE p_book_id = book_id;
		ELSE
			SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error Occured';
		END IF;
	COMMIT;
END;

DELIMITER //