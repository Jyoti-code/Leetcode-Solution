-- https://leetcode.com/problems/find-followers-count/description/

# Write your MySQL query statement below
select distinct user_id,count(distinct follower_id) as followers_count from Followers
group by user_id order by user_id;