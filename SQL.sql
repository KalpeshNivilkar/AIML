DROP DATABASE college;
CREATE DATABASE students;
SHOW DATABASES;
USE students;
-- parent table
CREATE TABLE st_info(
roll_no INT PRIMARY KEY,
name VARCHAR(20),
marks FLOAT
);

CREATE TABLE city_info(
city_name VARCHAR(20),
city_id INT,
FOREIGN KEY(city_id) references st_info(roll_no)
);

SHOW TABLES;

INSERT INTO st_info values(102,"sham",56.7);
SELECT *FROM st_info;
INSERT INTO city_info values ("punjab", 102);
SELECT *FROM st_info;
SELECT * FROM city_info;

-- default values

CREATE TABLE temp(
id INT,
salary INT DEFAULT 20000
);
INSERT INTO temp(id) VALUES(8);
SELECT * FROM temp;

-- unique
CREATE TABLE temp2(
id INT UNIQUE,
name VARCHAR(20)
);
INSERT INTO temp2 VALUES(101,"ram"),(102,"sham");
SELECT * FROM temp2;
INSERT INTO temp2 VALUES(102,"ram");

-- check 
CREATE TABLE temp3(
id INT,
name VARCHAR(30),
age FLOAT,
CONSTRAINT AGE_CHECK CHECK (age >= 18)
);
INSERT INTO temp3 VALUES(101,"ram",20);
SELECT * FROM temp3;
INSERT INTO temp3 VALUES(101,"ram",17);
SELECT * FROM temp3;
