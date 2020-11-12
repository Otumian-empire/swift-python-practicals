-- file_db.sql - the sql statements for ex25
-- Note that, the same database will be used
-- for all parts under ex25, but different tables
-- 
-- 
-- DATABASE=file_db
-- create file_db as a database with sqlite DB browser
CREATE DATABASE IF NOT EXISTS file_db;

-- create table for part1.py, file_stat
-- NOTE: To commit table is programmatically or through SQLite DB Browser
-- or expect this error, sqlite3.OperationalError: no such table: file_stat
CREATE TABLE "file_stat" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "file_name" TEXT NOT NULL,
    "num_chars" INTEGER NOT NULL,
    "num_lines" INTEGER NOT NULL,
    "created_at" TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- insert into file_stat
INSERT INTO
    file_stat(file_name, num_chars, num_lines)
VALUES
    (?, ?, ?);

-- the values will be passed a tuple to prevent sql-injections
-- there are 3 slots just for the 3 files
--
-- read the save file_stats
SELECT
    id,
    file_name,
    num_chars,
    num_lines
FROM
    file_stat;

-- 
-- create table for part2.py, file_stat2
-- table file_stat2: id, file_name, num_lines, num_words, chars_ws, chars_wos , created_at
CREATE TABLE IF NOT EXISTS "file_stat" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "file_name" TEXT NOT NULL,
    "num_lines" INTEGER NOT NULL,
    "num_words" INTEGER NOT NULL,
    "chars_ws" INTEGER NOT NULL,
    "chars_wos" INTEGER NOT NULL,
    "created_at" TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);