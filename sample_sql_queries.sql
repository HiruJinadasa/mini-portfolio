-- sample_sql_queries.sql

-- Create sample table
CREATE TABLE employees (
    id INT,
    name VARCHAR(50),
    department VARCHAR(50),
    salary INT
);

-- Insert sample data
INSERT INTO employees VALUES
(1, 'Alice', 'HR', 4000),
(2, 'Bob', 'IT', 5000),
(3, 'Charlie', 'Finance', 4500);

-- Query: Get all IT employees
SELECT * FROM employees WHERE department = 'IT';

-- Query: Average salary
SELECT AVG(salary) AS average_salary FROM employees;
