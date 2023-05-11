-- https://leetcode.com/problems/swap-salary/description/

# Write your MySQL query statement below
update Salary set 
sex= case sex when 'm' then 'f' 
else 'm' end;