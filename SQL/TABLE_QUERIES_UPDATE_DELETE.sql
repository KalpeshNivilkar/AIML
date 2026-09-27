
 -- table queries
CREATE DATABASE college8;
USE college8;

CREATE TABLE student (
    rollno INT PRIMARY KEY,
    name VARCHAR(50),
    marks INT NOT NULL,
    grade VARCHAR(1),
    city VARCHAR(20)
);
INSERT INTO student
(rollno, name, marks, grade, city)
VALUES
(101, "anil", 78, "C", "Pune"),
(102, "bhumika", 93, "A", "Mumbai"),
(103, "chetan", 85, "B", "Mumbai"),
(104, "dhruv", 96, "A", "Delhi"),
(105, "emanuel", 12, "F", "Delhi"),
(106, "farah", 82, "B", "Delhi");

SELECT * FROM student;

SET SQL_SAFE_UPDATES = 0;
UPDATE student 
SET grade = "O"
WHERE grade = "A";

SELECT * FROM student;

UPDATE student 
SET marks = 98
WHERE rollno = 105;
SELECT * FROM student;


UPDATE student 
SET grade = "A"
WHERE marks BETWEEN 70 AND 100;
SELECT * FROM student;

-- DELETE 

DELETE FROM student
WHERE marks < 80;
SELECT * FROM student;
