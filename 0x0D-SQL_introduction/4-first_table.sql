-- Create a Database, script should not fail if it already exists

USE hbtn_0c_0;
CREATE TABLE IF NOT EXISTS first_table(
	id INT ,
	name VARCHAR(256)
);

