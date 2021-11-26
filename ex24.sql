-- use the DB Browser to create some tables and experiment with it
--
-- create a database, ex25
CREATE DATABASE ex25;

-- create table users with id, fullname, dateofbirth and created_at as
CREATE TABLE "users" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "fullname" TEXT NOT NULL,
    "dateofbirth" TEXT NOT NULL,
    "created_at" TEXT NOT NULL DEFAULT current_timestamp
);

-- perform a crud on users table
-- INSERT(create)
INSERT INTO
    users(fullname, dateofbirth)
VALUES
    ("Derek Brundson", "12-12-1987"),
    ("Khabib Nurmagomedov", "10-12-1988"),
    ("Islam Makhachev", "27-08-1991"),
    ("Khamzat Chimaev", "02-02-1987"),
    ("Israel Adesanya", "12-09-1997"),
    ("Anderson Silver", "12-07-1988"),
    ("Rob Wilkinson", "12-12-1987"),
    ("Paulo Costa", "12-12-1988"),
    ("Brad Tavares", "12-12-1987"),
    ("Marvin Vettori", "12-12-1988"),
    ("Robert Whittaker", "12-12-1987"),
    ("Yoel Romero", "12-12-1988"),
    ("Dibir Zagirov", "12-12-1987");

-- SELECT(read) all from the users table
SELECT
    *
FROM
    users;

-- SELECT(read) the fullname of all users
SELECT
    fullname
FROM
    users;

-- SELECT(read) the dateofbirth and created_at, of all the users
SELECT
    dateofbirth,
    created_at
FROM
    users;

-- UPDATE, change all the users fullname to "Yamaha Tanaka" 
-- for all users with id > 2 
UPDATE
    users
SET
    fullname = "Yamaha Tanaka"
WHERE
    id > 2;

-- UPDATE, change all the users created_at to the current timestamp
-- for all users with id < 2 
UPDATE
    users
SET
    created_at = CURRENT_TIMESTAMP
where
    id < 4;


-- UPDATE, dateofbirth to "02-02-1990" for user with 
-- fullname = "Israel Adesanye"
UPDATE
    users
SET
    dateofbirth = "02-02-1990"
WHERE
    fullname = "Israel Adesanye";

-- DELETE, delete all users that have "ar" in their fullname
DELETE FROM
    users
WHERE
    fullname like "%ar%";

-- DELETE, delete user with id = 9
DELETE FROM
    users
WHERE
    id = 9;

-- DELETE, the end, delete everything in the users table
DELETE FROM
    users;