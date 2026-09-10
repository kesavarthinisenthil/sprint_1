CREATE DATABASE IF NOT EXISTS sprint1_db;

USE sprint1_db;


-- Departments table
CREATE TABLE IF NOT EXISTS departments (
    department_id INT PRIMARY KEY AUTO_INCREMENT,
    department_name VARCHAR(100) NOT NULL
);


-- Employees table
CREATE TABLE IF NOT EXISTS employees (
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    employee_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    department_id INT,
    salary DECIMAL(10, 2),
    joining_date DATE,
    FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);


-- Projects table
CREATE TABLE IF NOT EXISTS projects (
    project_id INT PRIMARY KEY AUTO_INCREMENT,
    project_name VARCHAR(100) NOT NULL,
    start_date DATE,
    end_date DATE
);


-- Employee Projects table
CREATE TABLE IF NOT EXISTS employee_projects (
    employee_id INT,
    project_id INT,
    assigned_date DATE,
    PRIMARY KEY (employee_id, project_id),
    FOREIGN KEY (employee_id)
        REFERENCES employees(employee_id),
    FOREIGN KEY (project_id)
        REFERENCES projects(project_id)
);


-- Tasks table
CREATE TABLE IF NOT EXISTS tasks (
    task_id INT PRIMARY KEY AUTO_INCREMENT,
    task_name VARCHAR(150) NOT NULL,
    employee_id INT,
    project_id INT,
    status VARCHAR(50),
    priority VARCHAR(50),
    FOREIGN KEY (employee_id)
        REFERENCES employees(employee_id),
    FOREIGN KEY (project_id)
        REFERENCES projects(project_id)
);