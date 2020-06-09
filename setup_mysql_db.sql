DROP DATABASE IF EXISTS mynd;
CREATE DATABASE IF NOT EXISTS mynd;
CREATE USER IF NOT EXISTS 'mynd_user'@'localhost' IDENTIFIED BY 'mynd';
GRANT ALL PRIVILEGES ON `mynd`.* TO 'mynd_user'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'mynd_user'@'localhost';
