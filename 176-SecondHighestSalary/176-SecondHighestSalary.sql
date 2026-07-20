-- Last updated: 20/07/2026, 18:39:23
# Write your MySQL query statement below
select MAX(salary) AS SecondHighestSalary from employee
where salary<(
    select MAX(salary) from employee
);