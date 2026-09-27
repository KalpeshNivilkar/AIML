CREATE TABLE employees (
    EmpID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Department VARCHAR(50),
    Salary DECIMAL(10,2),
    HireDate DATE
);

INSERT INTO employees (EmpID, FirstName, LastName, Department, Salary, HireDate)
VALUES
(101, 'Alice', 'Johnson', 'IT', 6500, '2020-03-15'),
(102, 'Mark', 'Rivera', 'HR', 4800, '2019-07-22'),
(103, 'Sophia', 'Lee', 'Finance', 7200, '2021-01-10'),
(104, 'Daniel', 'Kim', 'IT', 5800, '2018-11-05'),
(105, 'Emma', 'Brown', 'Marketing', 5300, '2022-04-18'),
(106, 'Liam', 'Patel', 'Finance', 6900, '2020-09-29'),
(107, 'Olivia', 'Garcia', 'HR', 4600, '2017-06-30'),
(108, 'Noah', 'Thompson', 'IT', 7500, '2023-02-12'),
(109, 'Ava', 'Martinez', 'Marketing', 5100, '2019-12-02'),
(110, 'Ethan', 'Davis', 'Finance', 8000, '2016-05-14');

-- Q1. Write a query to display every employee and all their data.
SELECT * FROM employees;

-- Q2. List only the FirstName, LastName, and Salary of every employee.
SELECT FirstName, LastName, Salary
FROM employees;

-- Q3. Show all employees who work in the 'IT' department
SELECT * 
FROM employees
WHERE Department = "IT";

-- Q4. Retrieve employees with a salary greater than 6000.
SELECT *
FROM employees
WHERE Salary > 6000;

-- Q5. List all employees ordered by HireDate from newest to oldest.
SELECT *
FROM employees
ORDER BY HireDate DESC;

-- Q6. Show a list of all unique departments present in the table.
SELECT Department 
FROM employees
GROUP BY Department;

-- Q7. Find employees whose first name starts with ‘Aʼ.
SELECT * 
FROM employees
WHERE FirstName like("A%");

-- Q8. Show employees whose salaries are between 4000 and 7000.
SELECT * 
FROM employees
WHERE Salary BETWEEN 4000 AND 7000;

-- Q9. Find the average salary of all employees.
SELECT AVG(Salary)
FROM employees;

/*Q10. List each department along with the number of employees, but only include departments 
with more than 3 employees.*/

SELECT Department, COUNT(EmpID)
FROM employees
GROUP BY Department
HAVING COUNT(EmpID) > 2;