USE sprint1_db;


-- ============================================
-- SAMPLE DATA
-- ============================================

INSERT INTO departments (department_name)
VALUES
('AI/ML'),
('Software Development'),
('Data Analytics');


INSERT INTO employees
    (employee_name, email, department_id, salary, joining_date)
VALUES
('Kesavarthini', 'kesavarthini@example.com', 1, 45000, '2026-07-06'),
('Arun', 'arun@example.com', 2, 40000, '2026-06-15'),
('Priya', 'priya@example.com', 1, 50000, '2026-05-10'),
('Rahul', 'rahul@example.com', 3, 55000, '2026-04-20'),
('Divya', 'divya@example.com', 3, 48000, '2026-03-12');


INSERT INTO projects
    (project_name, start_date, end_date)
VALUES
('Financial Services AI', '2026-07-01', NULL),
('Customer Portal', '2026-06-01', NULL),
('Data Analytics Platform', '2026-05-01', NULL);


INSERT INTO employee_projects
    (employee_id, project_id, assigned_date)
VALUES
(1, 1, '2026-07-06'),
(2, 2, '2026-06-15'),
(3, 1, '2026-05-10'),
(4, 3, '2026-04-20'),
(5, 3, '2026-03-12');


INSERT INTO tasks
    (task_name, employee_id, project_id, status, priority)
VALUES
('Data preprocessing', 1, 1, 'Completed', 'High'),
('Build ML model', 3, 1, 'In Progress', 'High'),
('API development', 2, 2, 'Completed', 'Medium'),
('Data analysis', 4, 3, 'In Progress', 'High'),
('Dashboard development', 5, 3, 'Pending', 'Medium');


-- ============================================
-- BASIC QUERIES
-- ============================================

SELECT *
FROM employees;

SELECT employee_name, salary
FROM employees
WHERE salary > 45000;

SELECT employee_name, salary
FROM employees
ORDER BY salary DESC;

SELECT department_id, COUNT(*) AS employee_count
FROM employees
GROUP BY department_id;

SELECT AVG(salary) AS average_salary
FROM employees;


-- ============================================
-- JOINS
-- ============================================

SELECT
    e.employee_name,
    d.department_name,
    e.salary
FROM employees e
INNER JOIN departments d
    ON e.department_id = d.department_id;


SELECT
    d.department_name,
    e.employee_name
FROM departments d
LEFT JOIN employees e
    ON d.department_id = e.department_id;


SELECT
    e.employee_name,
    d.department_name
FROM departments d
RIGHT JOIN employees e
    ON d.department_id = e.department_id;


SELECT
    e.employee_name,
    p.project_name
FROM employees e
INNER JOIN employee_projects ep
    ON e.employee_id = ep.employee_id
INNER JOIN projects p
    ON ep.project_id = p.project_id;


-- ============================================
-- UNION AND CASE
-- ============================================

SELECT employee_name AS name
FROM employees

UNION

SELECT project_name AS name
FROM projects;


SELECT
    employee_name,
    salary,
    CASE
        WHEN salary >= 50000 THEN 'High'
        WHEN salary >= 40000 THEN 'Medium'
        ELSE 'Low'
    END AS salary_category
FROM employees;


-- ============================================
-- SUBQUERIES
-- ============================================

SELECT employee_name, salary
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);


SELECT employee_name, salary
FROM employees
WHERE department_id = (
    SELECT department_id
    FROM departments
    WHERE department_name = 'AI/ML'
);


-- ============================================
-- CTE
-- ============================================

WITH department_salary AS (
    SELECT
        department_id,
        AVG(salary) AS average_salary
    FROM employees
    GROUP BY department_id
)
SELECT
    d.department_name,
    ds.average_salary
FROM department_salary ds
INNER JOIN departments d
    ON ds.department_id = d.department_id;


-- ============================================
-- WINDOW FUNCTIONS
-- ============================================

SELECT
    employee_name,
    salary,
    ROW_NUMBER() OVER (
        ORDER BY salary DESC
    ) AS row_num
FROM employees;


SELECT
    employee_name,
    salary,
    RANK() OVER (
        ORDER BY salary DESC
    ) AS salary_rank
FROM employees;


SELECT
    employee_name,
    salary,
    DENSE_RANK() OVER (
        ORDER BY salary DESC
    ) AS salary_dense_rank
FROM employees;


SELECT
    employee_name,
    salary,
    LAG(salary) OVER (
        ORDER BY salary
    ) AS previous_salary
FROM employees;


SELECT
    employee_name,
    salary,
    LEAD(salary) OVER (
        ORDER BY salary
    ) AS next_salary
FROM employees;


-- ============================================
-- INDEX
-- ============================================

CREATE INDEX idx_employee_department
ON employees(department_id);


-- ============================================
-- VIEW
-- ============================================

CREATE OR REPLACE VIEW employee_department_view AS
SELECT
    e.employee_id,
    e.employee_name,
    d.department_name,
    e.salary
FROM employees e
INNER JOIN departments d
    ON e.department_id = d.department_id;


-- Test the view
SELECT *
FROM employee_department_view;


-- ============================================
-- EXPLAIN
-- ============================================

EXPLAIN
SELECT
    e.employee_name,
    d.department_name
FROM employees e
INNER JOIN departments d
    ON e.department_id = d.department_id
WHERE e.department_id = 1;