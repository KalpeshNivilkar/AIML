CREATE DATABASE college4;
USE college4;

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

-- AGGREGATE FUNCTION
SELECT * FROM student;
SELECT marks FROM student;
SELECT MAX(marks) FROM student;
SELECT MIN(marks) FROM student;
SELECT AVG(marks) FROM student;
SELECT COUNT(rollno) FROM student;