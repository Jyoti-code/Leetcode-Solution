-- https://leetcode.com/problems/customers-who-bought-all-products/description/?envType=study-plan-v2&id=top-sql-50

# Write your MySQL query statement below
select customer_id from Customer
group by customer_id 
having count(distinct product_key)=(select count(distinct product_key)
from Product);