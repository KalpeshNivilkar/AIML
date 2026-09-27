CREATE DATABASE college;
USE college;

CREATE TABLE department (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL
);

CREATE TABLE teacher (
    teacher_id INT PRIMARY KEY,
    teacher_name VARCHAR(100) NOT NULL,
    department_id INT,
    
    FOREIGN KEY (department_id)
    REFERENCES department(department_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);


INSERT INTO department (department_id, department_name)
VALUES
(1, 'Computer Science'),
(2, 'AI & Data Science'),
(3, 'Information Technology');

UPDATE department
SET department_id = 4
WHERE department_id = 3;

INSERT INTO teacher (teacher_id, teacher_name, department_id)
VALUES
(101, 'Rahul', 1),
(102, 'Priya', 2),
(103, 'Amit', 3);


SELECT * FROM department;
SELECT * FROM teacher;
SELECT * FROM department;
SELECT * FROM teacher;

