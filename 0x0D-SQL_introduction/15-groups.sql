-- File: 14-average.sql
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
