-- https://leetcode.com/problems/find-users-with-valid-e-mails/description/

select * from Users
where mail REGEXP '^[a-zA-Z][a-zA-Z0-9\\-_.]*@leetcode\\.com$'