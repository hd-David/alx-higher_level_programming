-- Create the MySQL server user user_0d_1 if it doesn't already exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'%' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to the user_0d_1 user on all databases and tables
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'%';

-- Flush privileges to apply the changes
FLUSH PRIVILEGES;
