# Employee Salary Analysis

## Problem Statement

A company maintains employee records containing Employee ID, Department, and Salary.

The HR department wants to analyze employee salaries and identify employees whose salary is higher than the average salary of their respective department.

### Requirements

1. Calculate the average salary for each department.
2. Identify employees whose salary is above their department's average salary.
3. Display the department-wise average salary.
4. Display the employees earning above the department average.

## Sample Data

| Employee ID | Department | Salary |
| ----------- | ---------- | -----: |
| E101        | IT         |  45000 |
| E102        | IT         |  60000 |
| E103        | HR         |  40000 |
| E104        | HR         |  55000 |

## Formula

**Average Salary = Total Salary of Department ÷ Number of Employees in Department**

## Expected Output

IT Average Salary: 52500

Employee above IT average: E102

HR Average Salary: 47500

Employee above HR average: E104

## Approach

1. Store the employee records.
2. Group employees according to their department.
3. Calculate the total salary for each department.
4. Calculate the average salary for each department.
5. Compare each employee's salary with their department average.
6. Display employees whose salary is above the department average.

## Key Learning

This problem demonstrates how Python can be used to process structured employee data, perform calculations, group information, and apply conditional logic to solve a real-world business problem.
