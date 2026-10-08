# SQL 50 — Basic Aggregate Functions

| # | Problem | Pattern |
| ---: | --- | --- |
| 620 | Not Boring Movies | filter + modulo, not really an aggregate |
| 1251 | Average Selling Price | weighted avg, LEFT JOIN, COALESCE |
| 1075 | Project Employees I | AVG after JOIN, GROUP BY |
| 1633 | Percentage of Users Attended a Contest | count / total users, CROSS or scalar subquery |
| 1211 | Queries Quality and Percentage | AVG of ratio, AVG of CASE |
| 1193 | Monthly Transactions I | date bucket + several conditional SUMs |
| 1174 | Immediate Food Delivery II | first-order grain, then a rate |
| 550 | Game Play Analysis IV | first login + “logged in next day” rate |

1174 and 550 are the hard ones. They are “find a first event, then measure something about it.”
