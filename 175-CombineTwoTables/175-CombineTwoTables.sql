-- Last updated: 21/07/2026, 20:18:06
# Write your MySQL query statement below
select firstName,lastName,city,state 
from Person p
left join Address a
on p.personId=a.personId
