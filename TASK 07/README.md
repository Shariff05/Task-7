
# Task 7 - Walmart Sales Summary Using SQLite and Python

## Overview

This task involves:
- Using Python and SQLite to summarize sales data from a Walmart dataset.
- Creating a SQLite database from CSV data.
- Running SQL queries inside Python.
- Visualizing results using matplotlib.

## Steps Performed
1. Loaded Walmart sales data.
2. Simulated a `quantity` column (assuming avg price = $20).
3. Created `sales_data.db` and inserted data into a `sales` table.
4. Queried the database to get total quantity and revenue per store.
5. Plotted revenue as a bar chart using matplotlib.

## Tools Used
- pandas
- sqlite3
- matplotlib

## Output Files
- `sales_data.db`: SQLite database
- `sales_chart.png`: Revenue bar chart
- `task7_script.py`: Python script for the task

## How to Run
```bash
pip install pandas matplotlib
python task7_script.py
```
