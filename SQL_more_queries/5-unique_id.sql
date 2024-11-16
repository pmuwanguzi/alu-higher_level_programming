--a script that creates the table unique_id on your MySQL server.
USE hbtn_test_db_5;
CREATE TABLE IF NOT EXISTS unique_id (id INT UNIQUE DEFAULT 1, name VARCHAR(256));
