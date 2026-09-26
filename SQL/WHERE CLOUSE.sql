CREATE DATABASE college1;
USE college1;

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

SELECT DISTINCT city FROM student;
-- WHERE CLOUSE

SELECT * 
FROM student
WHERE city = "Delhi";

SELECT * FROM student WHERE grade = "A";
SELECT * FROM student WHERE grade = "A" and city = "Delhi";

-- logical operation on where clouse
SELECT * FROM student WHERE marks >= 90 AND city = "Delhi";

SELECT * FROM student WHERE marks > 90 OR city = "Delhi";

SELECT * FROM student WHERE marks BETWEEN 70 AND 100;

SELECT * FROM student WHERE marks IN("Delhi", "Pune");

SELECT * FROM student WHERE city NOT IN ("Delhi", "Pune");