-- Display score and score grouping counts

SELECT score, COUNT(score) AS number 
	FROM second_table 
	GROUP BY score 
	ORDER BY number DESC;
