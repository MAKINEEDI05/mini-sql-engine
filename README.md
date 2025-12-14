# Mini SQL Engine

A simplified in-memory SQL query engine built from scratch using Python.  
This project demonstrates how basic SQL queries are parsed and executed internally
by a database system using core data structures and algorithms.

---

## Features

- Load CSV files into memory
- Execute basic SQL SELECT queries
- Support for WHERE clause with a single condition
- Support for COUNT(*) and COUNT(column) aggregation
- Interactive Command-Line Interface (CLI)
- Clear error handling for invalid queries

---

## Project Structure

```text
mini-sql-engine/
│
├── cli.py          # Command-line interface (REPL)
├── parser.py       # SQL parsing logic
├── engine.py       # Query execution engine
├── loader.py       # CSV loading logic
├── errors.py       # Reserved for custom errors
├── data/           # Sample CSV files
├── README.md
└── .gitignore
````

---

## How to Run

### Requirements

* Python 3.8 or higher

### Steps

Run the CLI application:

```bash
python cli.py
```

When prompted, enter the path to a CSV file:

```text
data/students.csv
```

You can then start entering SQL queries interactively.

To exit the CLI, type:

```text
exit
```

or

```text
quit
```

---

## Supported SQL Grammar

The engine supports the following subset of SQL:

### SELECT all columns

```sql
SELECT * FROM students;
```

### SELECT specific columns

```sql
SELECT name, marks FROM students;
```

### WHERE clause (single condition)

```sql
SELECT name FROM students WHERE marks > 80;
```

### COUNT aggregation

```sql
SELECT COUNT(*) FROM students;
```

```sql
SELECT COUNT(marks) FROM students WHERE marks >= 85;
```

---

## Supported Operators

The WHERE clause supports the following comparison operators:

* `=`
* `!=`
* `>`
* `<`
* `>=`
* `<=`

---

## Limitations

This engine is intentionally limited for learning purposes:

* Only one table (single CSV file) is supported
* Only SELECT queries are supported
* Only one WHERE condition is allowed
* No JOIN, GROUP BY, ORDER BY, or subqueries
* No INSERT, UPDATE, or DELETE operations

---

## Sample Data

Sample CSV files are provided in the `data/` directory:

* `students.csv`
* `employees.csv`

These files are used for testing and demonstration purposes.

---

## Error Handling

The engine gracefully handles:

* Invalid SQL syntax
* Queries on non-existent columns
* Type mismatches in WHERE conditions
* Unsupported SQL features

Errors are reported with clear, user-friendly messages without crashing the program.

---

## Design Choices

* CSV data is loaded into memory as a list of dictionaries for intuitive row-wise processing
* SQL parsing is implemented using simple string operations for clarity and readability
* Query execution follows a logical pipeline:
  **FROM → WHERE → AGGREGATION → SELECT**
* No external SQL or parsing libraries are used to emphasize core algorithmic understanding

---
