# Sprint 1 – Python, OOPs and SQL Competency Assessment

## Project Overview

This project demonstrates Python programming, Object-Oriented Programming (OOP), SQL, exception handling, logging, utility functions, and modular development.

The project was developed as part of the AI/ML Engineer Sprint 1 competency assessment.

## Technologies Used

* Python
* MySQL
* MySQL Workbench
* VS Code
* Git and GitHub

## Project Structure

```text
Sprint 1/
│
├── src/
│   ├── __init__.py
│   ├── loader.py
│   ├── writer.py
│   ├── database.py
│   ├── logger.py
│   ├── config.py
│   ├── utils.py
│   └── exceptions.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── data/
├── logs/
├── outputs/
├── tests/
│
├── main.py
├── requirements.txt
└── README.md
```

## Python Modules

### DataLoader

* Loads CSV, JSON, and TXT files.
* Validates file paths.
* Handles unsupported file formats.

### DataWriter

* Writes data to CSV, JSON, TXT, and Pickle files.
* Handles file-writing errors.

### DatabaseConnector

* Connects the Python application to MySQL.
* Handles database connection errors.

### LoggerManager

* Provides application logging.
* Supports INFO, WARNING, and ERROR messages.
* Logs are stored in `logs/application.log`.

### ConfigManager

Demonstrates:

* Inheritance
* Encapsulation
* Properties
* Class methods
* Type hints

### Utility Functions

Includes:

* Timestamp generation
* File validation
* Path validation
* Configuration value reading
* Logger helper
* Execution time decorator

## Exception Handling

Custom exceptions implemented:

* `InvalidFileException`
* `DatabaseConnectionException`

The project uses `try`, `except`, `finally`, and `raise` for error handling.

## SQL

The database contains five related tables:

1. Departments
2. Employees
3. Projects
4. Employee Projects
5. Tasks

SQL concepts demonstrated:

* SELECT
* WHERE
* GROUP BY
* ORDER BY
* INNER JOIN
* LEFT JOIN
* RIGHT JOIN
* UNION
* CASE
* Subqueries
* CTE
* ROW_NUMBER
* RANK
* DENSE_RANK
* LAG
* LEAD
* Indexes
* Views
* EXPLAIN

## How to Run

Install the required dependency:

```bash
pip install -r requirements.txt
```

Configure the MySQL credentials in `main.py`.

Run the application:

```bash
python main.py
```

## Database Setup

The database schema is available in:

```text
sql/schema.sql
```

SQL queries and sample data are available in:

```text
sql/queries.sql
```

The SQL scripts can be executed using MySQL Workbench.

## Logging

Application logs are stored in:

```text
logs/application.log
```

The logs record important application events such as file operations and database connection status.

## Key Learnings

* Python modular programming
* Object-Oriented Programming
* Exception handling
* Logging
* File processing
* MySQL connectivity
* SQL joins and queries
* Window functions
* Database optimization
* Git/GitHub project organization
