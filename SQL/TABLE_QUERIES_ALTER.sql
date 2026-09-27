-- ALTER TABLE
CREATE DATABASE IF NOT EXISTS department;
USE department;
CREATE TABLE IF NOT EXISTS dept(
id INT PRIMARY KEY,
name VARCHAR(30),
location VARCHAR(30)
);

INSERT INTO dept
VALUES( 101,"banking","pune");
INSERT INTO dept
VALUES( 102,"banking","punjab");

SELECT * FROM dept;

-- ADD COLUMN
ALTER TABLE dept
ADD COLUMN years INT DEFAULT 2003;

-- DROP COLUMN
ALTER TABLE dept
DROP COLUMN years;

-- MODIFY COLUMN
ALTER TABLE dept
MODIFY id VARCHAR(10);

-- RENAME TABLE
ALTER TABLE dept
RENAME TO department;

SHOW TABLES;

-- CHANGE COLUMN (RENAME)
ALTER TABLE department
CHANGE id dept_id INT;

SELECT * FROM department;  

-- name to full name
ALTER TABLE department
CHANGE name full_name VARCHAR(20);

-- delete students who marks less than 1oo
SET SQL_SAFE_UPDATES = 0;
DELETE FROM department
WHERE location= "pune";

-- delete location column
ALTER TABLE department
DROP COLUMN location;
