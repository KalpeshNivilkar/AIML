-- union
CREATE DATABASE employees;
USE employees;

CREATE TABLE emp_info(
id INT PRIMARY KEY,
name VARCHAR(20)
);

CREATE TABLE emp_salary(
id INT,
salary FLOAT DEFAULT 20000,
FOREIGN KEY (id) REFERENCES emp_info(id)
);

INSERT INTO emp_info VALUES(101, "ramm"),(102, "shamm");
INSERT INTO emp_salary (id) VALUES(101),(102);
INSERT INTO emp_info VALUES (103,"ramm");
UPDATE emp_info
SET id = 104
WHERE id = 103;
SELECT * FROM emp_info;
SELECT * FROM emp_salary;

SELECT * FROM emp_info
UNION ALL
SELECT * FROM emp_info;