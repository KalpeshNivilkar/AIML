CREATE DATABASE student;

USE student;

CREATE TABLE student(
s_id INT PRIMARY KEY,
s_name VARCHAR(20)
);
ALTER TABLE student
MODIFY s_id INT NOT NULL;

CREATE TABLE course(
c_id INT,
c_name VARCHAR(20)
);

INSERT INTO student VALUES(101,"kalpesh"), (102,"ram");
INSERT INTO course VALUES(101,"AI"), (102,"STAT");
INSERT INTO course VALUES(106,"AI"), (107,"STAT");



SELECT * FROM student;
SELECT * FROM course;
INSERT INTO student VALUES(104,"kalpesh"), (105,"ram");
SELECT * FROM student;
-- inner join
SELECT * 
FROM student
INNER JOIN course
ON student.s_id = course.c_id;

-- left join
SELECT * 
FROM student as s
LEFT JOIN course as c
ON s.s_id = c.c_id;

-- right join
SELECT *
FROM student as s
RIGHT JOIN course as c
ON s.s_id =  c.c_id;

-- full join 
SELECT *
FROM student as s
LEFT JOIN course as c
ON s.s_id = c.c_id
UNION
SELECT * 
FROM student as s
RIGHT join course as c
ON s.s_id = c.c_id;

-- left exclusively join
SELECT *
FROM student as s
LEFT JOIN course as c
ON s.s_id = c.c_id
WHERE c.c_id IS NULL;

-- right exclusive join

SELECT * 
FROM student as s
RIGHT JOIN course as c
ON s.s_id = c.c_id
WHERE s.s_id IS NULL;

-- both
SELECT * 
FROM student as s
LEFT JOIN course as c
ON s.s_id = c.c_id
WHERE c.c_id IS NULL
UNION
SELECT *
FROM student as s
RIGHT JOIN course as c
ON s.s_id = c.c_id
WHERE s.s_id IS NULL;


