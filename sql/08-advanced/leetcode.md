# Advanced SQL 50

Official plan (Premium): https://leetcode.com/studyplan/premium-sql-50/

Grouped by the lesson that unlocks them. Numbers follow the common public list of that study plan.

## Select / CASE / simple filter

| # | Problem | Lesson |
| ---: | --- | --- |
| 1821 | Find Customers with Positive Revenue this Year | Select |
| 1873 | Calculate Special Bonus | CASE |
| 1890 | The Latest Login in 2020 | MAX / filter year |
| 1440 | Evaluate Boolean Expression | self-join lookup |

## Joins and anti-joins

| # | Problem | Lesson |
| ---: | --- | --- |
| 183 | Customers Who Never Order | anti-join |
| 175 | Combine Two Tables | LEFT JOIN |
| 1607 | Sellers With No Sales | anti-join |
| 607 | Sales Person | anti-join through a third table |
| 1407 | Top Travellers | LEFT JOIN + SUM |
| 1571 | Warehouse Manager | JOIN + SUM |
| 1965 | Employees With Missing Information | FULL / UNION of two antis |
| 1264 | Page Recommendations | friends-of-friends |

## Group / having

| # | Problem | Lesson |
| ---: | --- | --- |
| 511 | Game Play Analysis I | MIN date per player |
| 586 | Customer Placing the Largest Number of Orders | GROUP + MAX |
| 1741 | Find Total Time Spent by Each Employee | SUM |
| 1173 | Immediate Food Delivery I | rate |
| 1587 | Bank Account Summary II | HAVING sum |
| 182 | Duplicate Emails | GROUP HAVING count > 1 |
| 1050 | Actors and Directors Who Cooperated At Least Three Times | HAVING |
| 1693 | Daily Leads and Partners | count DISTINCT |
| 1699 | Number of Calls Between Two Persons | normalize pair, then SUM |

## Windows / top-n

| # | Problem | Lesson |
| ---: | --- | --- |
| 1112 | Highest Grade For Each Student | ROW_NUMBER / MAX |
| 184 | Department Highest Salary | rank = 1 |
| 1549 | The Most Recent Orders for Each Product | ROW_NUMBER |
| 1532 | The Most Recent Three Orders | ROW_NUMBER <= 3 |
| 1831 | Maximum Transaction Each Day | rank or MAX join |
| 1596 | The Most Frequently Ordered Products for Each Customer | RANK on counts |
| 1412 | Find the Quiet Students in All Exams | rank per exam |

## Unpivot / generate / consecutive

| # | Problem | Lesson |
| ---: | --- | --- |
| 1795 | Rearrange Products Table | unpivot |
| 1445 | Apples & Oranges | self-join or pivot diff |
| 603 | Consecutive Available Seats | neighbor |
| 613 | Shortest Distance in a Line | self-join abs |
| 1285 | Find the Start and End Number of Continuous Ranges | islands |
| 1225 | Report Contiguous Dates | islands |
| 1767 | Find the Subtasks That Did Not Execute | generate 1..n, anti-join |

## Trees

| # | Problem | Lesson |
| ---: | --- | --- |
| 608 | Tree Node | Root / Inner / Leaf |
| 1270 | All People Report to the Given Manager | recursive CTE |

If a title here does not match what you see on LeetCode, trust LeetCode and keep the pattern column. The point is the pattern, not the number.
