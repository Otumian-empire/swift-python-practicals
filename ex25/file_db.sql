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
-- create table for part3.py, bkpfile
-- table bkpfile: id, file_name, file_content, created_at
-- SInce this is basically to backup files, we do not need a 
-- duplicate of it, thus we make the file name unique
-- update file_content when file_name already exist and update thr create time.
CREATE TABLE IF NOT EXISTS "bkpfile" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "file_name" TEXT NOT NULL UNIQUE,
    "file_content" Text NOT NULL,
    "created_at" TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
) COMMIT;

-- insert
INSERT INTO
    bkpfile(file_name, file_content)
VALUES
    (?, ?);

-- read file_content by file name
SELECT
    file_content
FROM
    bkpfile
WHERE
    file_name = "";

-- read file_name and created_at for the screen
SELECT
    id,
    file_name,
    created_at
FROM
    bkpfile
WHERE
    file_name = "";

-- Update
UPDATE
    bkpfile
SET
    file_content = ?,
    created_at = CURRENT_TIMESTAMP
WHERE
    file_name = ?;