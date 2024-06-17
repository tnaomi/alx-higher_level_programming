-- Display only rows with non-null NAME values

SELECT score, name
	FROM second_table
	WHERE name != 'NULL'
	ORDER BY score DESC;
