# Exam ranks

**Pattern:** DENSE_RANK per group. **LeetCode cousins:** 185, 184.

## Table: `exams(name, department, score)`

## Task

Return `department`, `name`, `score`, and `score_rank`.

`score_rank` is `DENSE_RANK` inside the department, high score first. Ties share a rank. The next rank does not skip.

Order by `department`, then `score_rank`, then `name`.
