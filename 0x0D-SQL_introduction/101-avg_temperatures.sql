-- Display city, AVERAGE of temps in F

SELECT city, AVG(value) AS avg_temp 
	FROM temperatures
	GROUP BY city
	ORDER BY avg_temp DESC;
