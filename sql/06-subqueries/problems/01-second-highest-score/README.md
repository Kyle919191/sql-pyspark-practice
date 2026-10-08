# Second-highest score

**Pattern:** scalar subquery; NULL if it does not exist. **LeetCode cousin:** 176.

## Table: `exams(id, score)`

Scores can tie.

## Task

Return one column `second_highest`: the second distinct score. If there is no second distinct score, return NULL.

The result is always one row.
