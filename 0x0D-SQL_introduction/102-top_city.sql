-- Display city, AVERAGE of temps in F. Top 3 Cities

SELECT city, AVG(value) AS avg_temp 
	FROM temperatures
	WHERE month = 7 OR month = 8
	GROUP BY city
	ORDER BY avg_temp DESC
	LIMIT 3;
