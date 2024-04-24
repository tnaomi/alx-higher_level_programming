# 0x0D-SQL_introduction

## Author

Tadala Kapengule

## Tasks

### 0. List databases

Write a script that lists all databases of your MySQL server.

__File__

0-list_databases.sql

```bash
## To run
cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
```

### 1. Create a database

Write a script that creates the database ``hbtn_0c_0`` in your MySQL server.

- If the database ``hbtn_0c_0`` already exists, your script should not fail
- You are not allowed to use the ``SELECT`` or ``SHOW`` statements

__File__

1-create_database_if_missing.sql

```bash
## To run
cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
```

### 2. Delete a database

Write a script that **deletes the database** ``hbtn_0c_0`` in your MySQL server.

- If the database ``hbtn_0c_0`` doesn’t exist, your script should not fail
- You are not allowed to use the ``SELECT`` or ``SHOW`` statements

__File__

2-remove_database.sql

```bash
## To run
cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
```
### 3. List tables

Write a script that **lists all the tables** of a database in your MySQL server.

- The **database name** will be passed as argument of mysql command (in the following example: ``mysql`` is the name of the database)

__File__

3-list_tables.sql

```bash
# To run
cat 3-list_tables.sql | mysql -hlocalhost -uroot -p mysql
```

### 4. First table

Write a script that creates a table called ``first_table`` in the current database in your MySQL server.

- ``first_table`` description:
	- ``id`` INT
	- ``name`` VARCHAR(256)
- The **database name** will be passed as an argument of the mysql command
- If the table ``first_table`` already exists, your script should not fail
- You are not allowed to use the ``SELECT`` or ``SHOW`` statements

__File__

4-first_table.sql

```bash
# To run
cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

### 5. Full description

Write a script that prints the full description of the table ``first_table`` from the database ``hbtn_0c_0`` in your MySQL server.

- The **database name** will be passed as an argument of the mysql command
- You are not allowed to use the ``DESCRIBE`` or ``EXPLAIN`` statements

__File__

5-full_table.sql

```bash
# To run
cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

### 6. List all in table

Write a script that **lists all rows** of the table ``first_table`` from the database ``hbtn_0c_0`` in your MySQL server.

- All fields should be printed
- The **database name** will be passed as an argument of the mysql command

__File__

6-list_values.sql

```bash
# To run
cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

### 7. First add

Write a script that **inserts a new row** in the table ``first_table`` (``database hbtn_0c_0``) in your MySQL server.

- New row:
	- ``id`` = 89
	- ``name`` = Best School
- The **database name** will be passed as an argument of the mysql command

__File__

7-insert_value.sql

```bash
# To run
cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

### 8. Count 89

Write a script that **displays the number of records** with ``id`` = ``89`` in the table ``first_table`` of the database ``hbtn_0c_0`` in your MySQL server.

- The **database name** will be passed as an argument of the mysql command

__File__

8-count_89.sql

```bash
# To run
cat 8-count_89.sql | mysql -hlocalhost -uroot -p hbtn_0c_0 | tail -1
```

### 9. Full creation

Write a script that **creates a table** ``second_table`` in the database ``hbtn_0c_0`` in your MySQL server and **add multiples rows**.

- second_table description:
	- ``id`` INT
	- ``name`` VARCHAR(256)
	- ``score`` INT
- The **database name** will be passed as an argument to the mysql command
- If the table ``second_table`` already exists, your script should not fail
- You are not allowed to use the ``SELECT`` and ``SHOW`` statements
- Your script should create these records:
	- ``id`` = ``1``, ``name``= “``John``”, ``score`` = ``10``
	- ``id`` = ``2``, ``name`` = “``Alex``”, ``score`` = ``3``
	- ``id`` = ``3``, ``name`` = “``Bob``”, ``score`` = ``14``
	- ``id`` = ``4``, ``name`` = “``George``”, ``score`` = ``8``

__File__

9-full_creation.sql

```bash
# To run
cat 9-full_creation.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

### 10. List by best

Write a script that **lists all records** of the table ``second_table`` of the database ``hbtn_0c_0`` in your MySQL server.

- Results should display both the ``score`` and the ``name`` (in this order)
- Records should be ordered by ``score`` (top first)
- The **database name** will be passed as an argument of the mysql command

__File__

10-top_score.sql

```bash
#To run
cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

### 11. Select the best

Write a script that **lists all records with a ``score`` >= 10** in the table ``second_table`` of the database ``hbtn_0c_0`` in your MySQL server.

- Results should display both the ``score`` and the ``name`` (in this order)
- Records should be ordered by ``score`` (top first)
- The **database name** will be passed as an argument of the mysql command

__File__

11-best_score.sql

```bash
#To run
cat 11-best_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

### 12. Cheating is bad

Write a script that **updates the ``score``** of ``Bob`` to ``10`` in the table ``second_table``.

- You are **not** allowed to use Bob’s ``id`` value, only the ``name`` field
- The **database name** will be passed as an argument of the mysql command

__File__

12-no_cheating.sql

```bash
# To run
cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

### 13. Score too low

Write a script that **removes all records with a ``score`` <= ``5``** in the table ``second_table`` of the database ``hbtn_0c_0`` in your MySQL server.

- The **database name** will be passed as an argument of the mysql command

__File__

13-change_class.sql

```bash
# To run
cat 13-change_class.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

### 14. Average

Write a script that **computes the score average of all records** in the table ``second_table`` of the database ``hbtn_0c_0`` in your MySQL server.

- The result column name should be ``average``
- The **database name** will be passed as an argument of the mysql command

__File__

14-average.sql

```bash
#To run
cat 14-average.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

### 15. Number by score

Write a script that **lists the number of records with the same score** in the table ``second_table`` of the database ``hbtn_0c_0`` in your MySQL server.

- The result should display:
	- the ``score``
	- the number of records for this ``score`` with the label ``number``
- The list should be sorted by the number of records (descending)
- The **database name** will be passed as an argument to the mysql command

__File__

15-groups.sql

```bash
# To run
cat 15-groups.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

### 16. Say my name

Write a script that **lists all records** of the table ``second_table`` of the database ``hbtn_0c_0`` in your MySQL server.

- Don’t list rows without a ``name`` value
- Results should display the ``score`` and the ``name`` (in this order)
- Records should be listed by descending ``score``
- The **database name** will be passed as an argument to the mysql command

In this example, new data have been added to the table ``second_table``.

__File__

16-no_link.sql

```bash
# To run
cat 16-no_link.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

## Optional Tasks

### 17. Go to UTF8

Write a script that converts ``hbtn_0c_0`` database to ``UTF8`` (``utf8mb4``, ``collate utf8mb4_unicode_ci``) in your MySQL server.

You need to convert all of the following to ``UTF8``:

- Database ``hbtn_0c_0``
- Table ``first_table``
- Field ``name`` in ``first_table``

__File__

100-move_to_utf8.sql

```bash
# To run
cat 100-move_to_utf8.sql | mysql -hlocalhost -uroot -p
```

### 18. Temperatures #0

Import in ``hbtn_0c_0`` database this table dump: [``download``](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql)

Write a script that displays the average ``temperature`` (``Fahrenheit``) by ``city`` ordered by temperature (descending).

__File__

101-avg_temperatures.sql

```bash
# To run
cat 101-avg_temperatures.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

### 19. Temperatures #1

Import in ``hbtn_0c_0`` database this table dump: [``download``](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql)

Write a script that displays the top 3 of cities temperature during July and August ordered by ``temperature`` (descending)

__File__

102-top_city.sql

```bash
# To run
cat 102-top_city.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```

### 20. Temperatures #2

Import in ``hbtn_0c_0`` database this table dump: [``download``](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql)

Write a script that **displays the max temperature** of each state (ordered by ``State`` name).

__File__

103-max_state.sql

```bash
# To run
cat 103-max_state.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
```